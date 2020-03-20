
from itertools import groupby

from naeval.const import (
    DEEPPAVLOV,
    DEEPPAVLOV_BERT
)
from naeval.record import Record
from naeval.tokenizer import tokenize
from naeval.span import offset_spans

from ..bio import bio_spans
from ..markup import Markup
from ..adapt import adapt_deeppavlov

from .token import find_tokens
from .base import post, ChunkModel


DEEPPAVLOV_IMAGE = 'natasha/deeppavlov-ner-ru'
DEEPPAVLOV_CONTAINER_PORT = 5000

# requires ~10Gb GPU RAM
DEEPPAVLOV_SECTION = 256
DEEPPAVLOV_BATCH = 64

DEEPPAVLOV_URL = 'http://{host}:{port}/ner'

DEEPPAVLOV_BERT_IMAGE = 'natasha/deeppavlov-ner-ru-bert'
DEEPPAVLOV_BERT_CONTAINER_PORT = 5000

# ~9Gb
DEEPPAVLOV_BERT_SECTION = 256
DEEPPAVLOV_BERT_BATCH = 64


class DeeppavlovMarkup(Markup):
    @property
    def adapted(self):
        return adapt_deeppavlov(self)


########
#
#   SECTION
#
######


class Section(Record):
    __attributes__ = ['source', 'start', 'stop', 'text', 'spans']

    def __init__(self, source, start, stop, text, spans=None):
        self.source = source
        self.start = start
        self.stop = stop
        self.text = text
        self.spans = spans


def group_chunks(items, size):
    buffer = []
    for item in items:
        buffer.append(item)
        if len(buffer) >= size:
            yield buffer
            buffer = []
    if buffer:
        yield buffer


def split_sections(texts, size):
    for source, text in enumerate(texts):
        tokens = tokenize(text)
        chunks = group_chunks(tokens, size)
        for chunk in chunks:
            start, stop = chunk[0].start, chunk[-1].stop
            yield Section(
                source, start, stop,
                text[start:stop]
            )


def group_sections(sections):
    for _, group in groupby(sections, key=lambda _: _.source):
        yield group


def sections_markup(sections):
    chunks, spans = [], []
    stop = 0
    for section in sections:
        chunks.append(' ' * (section.start - stop))
        chunks.append(section.text)
        spans.extend(offset_spans(section.spans, section.start))
        stop = section.stop
    text = ''.join(chunks)
    return DeeppavlovMarkup(text, spans)


########
#
#  MAP
#
#####


DEEPPAVLOV_STRIP = r'\s'
DEEPPAVLOV_BERT_STRIP = r' '


def parse_deeppavlov(texts, data, mode=DEEPPAVLOV):
    strip = DEEPPAVLOV_STRIP
    if mode == DEEPPAVLOV_BERT:
        strip = DEEPPAVLOV_BERT_STRIP

    for text, (chunks, tags) in zip(texts, data):
        # see patch_texts
        if not text.strip():
            spans = []
        else:
            tokens = find_tokens(chunks, text, strip=strip)
            spans = list(bio_spans(tokens, tags))
        yield DeeppavlovMarkup(text, spans)


def call_deeppavlov(texts, host, port, mode=DEEPPAVLOV):
    url = DEEPPAVLOV_URL.format(
        host=host,
        port=port
    )
    payload = {'context': texts}
    response = post(
        url,
        json=payload
    )
    data = response.json()
    return parse_deeppavlov(texts, data, mode)


def patch_texts(texts):
    # deeppavlov does not work well with
    # texts=['', '\t', '   '] and so on
    for text in texts:
        if not text.strip():
            text = '?'  # assume ? is not tagged
        yield text


def map_batches(batches, host, port, mode=DEEPPAVLOV):
    for batch in batches:
        texts = [_.text for _ in batch]
        markups = call_deeppavlov(texts, host, port, mode)
        for section, markup in zip(batch, markups):
            section.spans = markup.spans
            yield section


def map_deepavlov(texts, host, port,
                  section_size=DEEPPAVLOV_SECTION, batch_size=DEEPPAVLOV_BATCH,
                  mode=DEEPPAVLOV):
    texts = patch_texts(texts)
    sections = split_sections(texts, section_size)
    batches = group_chunks(sections, batch_size)  # group sections for speed
    sections = map_batches(batches, host, port, mode)  # same sections with annotation
    groups = group_sections(sections)  # group by text
    for group in groups:
        yield sections_markup(group)


class DeeppavlovModel(ChunkModel):
    name = DEEPPAVLOV
    image = DEEPPAVLOV_IMAGE
    container_port = DEEPPAVLOV_CONTAINER_PORT

    def map(self, texts):
        return map_deepavlov(
            texts, self.host, self.port,
            DEEPPAVLOV_SECTION, DEEPPAVLOV_BATCH,
            mode=DEEPPAVLOV
        )


class DeeppavlovBERTModel(DeeppavlovModel):
    name = DEEPPAVLOV_BERT
    image = DEEPPAVLOV_BERT_IMAGE
    container_port = DEEPPAVLOV_BERT_CONTAINER_PORT

    # BERT version starts >2min
    retries = 100
    delay = 5

    def map(self, texts):
        return map_deepavlov(
            texts, self.host, self.port,
            DEEPPAVLOV_BERT_SECTION, DEEPPAVLOV_BERT_BATCH,
            mode=DEEPPAVLOV_BERT
        )
