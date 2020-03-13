
from itertools import groupby

from naeval.const import (
    DEEPPAVLOV,
    DEEPPAVLOV_BERT
)
from naeval.record import Record
from nerus.tokenizer import space_tokenize
from nerus.span import offset_spans

from ..bio import bio_spans
from ..markup import Markup
from ..adapt import adapt_deeppavlov

from .token import find_tokens
from .base import post, ChunkAnnotator


DEEPPAVLOV_IMAGE = 'natasha/deeppavlov-ner-ru'
DEEPPAVLOV_CONTAINER_PORT = 5000

DEEPPAVLOV_SECTION = 1000
DEEPPAVLOV_BATCH = 100

DEEPPAVLOV_URL = 'http://{host}:{port}/ner'

DEEPPAVLOV_BERT_IMAGE = 'natasha/deeppavlov-ner-ru-bert'
DEEPPAVLOV_BERT_CONTAINER_PORT = 5000

# assume 200 tokens split by whitespace < 512 bert tokens
DEEPPAVLOV_BERT_SECTION = 200
DEEPPAVLOV_BERT_BATCH = 100

DEEPPAVLOV_BERT_URL = 'http://{host}:{port}/ner'


class DeeppavlovMarkup(Markup):
    label = DEEPPAVLOV

    @property
    def adapted(self):
        return adapt_deeppavlov(self)


class DeeppavlovBERTMarkup(DeeppavlovMarkup):
    label = DEEPPAVLOV_BERT


class Section(Record):
    __attributes__ = ['source', 'start', 'stop', 'text']

    def __init__(self, source, start, stop, text, markup=None):
        self.source = source
        self.start = start
        self.stop = stop
        self.text = text

    def annotated(self, spans):
        return AnnotatedSection(
            self.source, self.start, self.stop,
            self.text, spans
        )


class AnnotatedSection(Section):
    __attributes__ = ['source', 'start', 'stop', 'text', 'spans']

    def __init__(self, source, start, stop, text, spans):
        Section.__init__(self, source, start, stop, text)
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


def section_texts(texts, size):
    for source, text in enumerate(texts):
        tokens = space_tokenize(text)
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


def merge_markups(cls, sections):
    chunks = []
    spans = []
    stop = 0
    for section in sections:
        chunks.append(' ' * (section.start - stop))
        chunks.append(section.text)
        spans.extend(offset_spans(section.spans, section.start))
        stop = section.stop
    text = ''.join(chunks)
    return cls.Markup(text, spans)


DEEPPAVLOV_STRIP = r'\s'
DEEPPAVLOV_BERT_STRIP = r' '


def parse(cls, texts, data):
    for text, (chunks, tags) in zip(texts, data):
        # see patch_texts
        if not text.strip():
            spans = []
        else:
            tokens = list(find_tokens(chunks, text, strip=cls.strip))
            spans = list(bio_spans(tokens, tags))
        yield cls.Markup(text, spans)


def call(cls, texts, host, port):
    url = cls.url.format(
        host=host,
        port=port
    )
    payload = {'context': texts}
    response = post(
        url,
        json=payload
    )
    data = response.json()
    return parse(cls, texts, data)


def patch_texts(texts):
    # deeppavlov does not work well with
    # texts=['', '\t', '   '] and so on
    for text in texts:
        if not text.strip():
            text = '?'  # assume ? is not tagged
        yield text


def map_(cls, batches, host, port):
    for sections in batches:
        texts = [_.text for _ in sections]
        data = call(cls, texts, host, port)
        markups = list(parse(cls, texts, data))
        for section, markup in zip(sections, markups):
            yield section.annotated(markup.spans)


def map(cls, texts, host, port,
        section_size=DEEPPAVLOV_SECTION, batch_size=DEEPPAVLOV_BATCH):
    texts = patch_texts(texts)
    sections = section_texts(texts, section_size)
    batches = group_chunks(sections, batch_size)
    sections = map_(cls, batches, host, port)
    groups = group_sections(sections)
    for group in groups:
        yield merge_markups(cls, group)


class DeeppavlovAnnotator(ChunkAnnotator):
    name = DEEPPAVLOV

    Markup = DeeppavlovMarkup

    def map(self, texts):
        return map(
            self, texts, self.host, self.port,
            self.section_size, self.batch_size
        )


class DeeppavlovBERTAnnotator(DeeppavlovAnnotator):
    name = DEEPPAVLOV_BERT

    # BERT version starts >2min, requires >3GB
    retries = 100
    delay = 5
