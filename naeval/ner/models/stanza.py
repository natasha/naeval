
import re

from naeval.const import STANZA
from naeval.span import (
    Span,
    envelop_spans,
    offset_spans
)
from naeval.sent import Sent
from naeval.chop import chop

from ..adapt import adapt_stanza
from ..markup import Markup

from .base import post, ChunkModel


STANZA_IMAGE = 'natasha/stanza-ru'
STANZA_CONTAINER_PORT = 8080
STANZA_URL = 'http://{host}:{port}/'
STANZA_BATCH = 32


class StanzaMarkup(Markup):
    label = STANZA

    @property
    def adapted(self):
        return adapt_stanza(self)


def parse_spans(data):
    for ent in data['entities']:
        yield Span(
            start=ent['start_char'],
            stop=ent['end_char'],
            type=ent['type']
        )


def parse_token_span(item):
    # {'id': '1', 'text': 'Путин', 'misc': 'start_char=0|end_char=5'}
    match = re.match(r'start_char=(\d+)\|end_char=(\d+)', item['misc'])
    start, stop = match.groups()
    return int(start), int(stop)


def parse_sents(texts, data):
    for text, sent in zip(texts, data['sentences']):
        first, last = sent[0], sent[-1]
        start, _ = parse_token_span(first)
        _, stop = parse_token_span(last)
        yield Sent(start, stop, text)


def sent_spans(sent, spans):
    spans = envelop_spans(sent, spans)
    return offset_spans(spans, -sent.start)


def parse_stanza(texts, data):
    spans = list(parse_spans(data))
    sents = parse_sents(texts, data)
    for sent in sents:
        yield StanzaMarkup(
            sent.text,
            list(sent_spans(sent, spans))
        )


def escape_text(text):
    return re.sub('[\n\r][\n\r]', '  ', text)


def stanza_payload(batch):
    return '\n\n'.join(
        escape_text(_)
        for _ in batch
    )


def call_stanza(texts, host, port):
    url = STANZA_URL.format(
        host=host,
        port=port
    )
    payload = stanza_payload(texts)
    response = post(url, json=payload)
    data = response.json()
    return parse_stanza(texts, data)


def map_stanza(texts, host, port, batch_size=STANZA_BATCH):
    batches = chop(texts, batch_size)
    for batch in batches:
        markups = call_stanza(batch, host, port)
        for markup in markups:
            yield markup


class StanzaModel(ChunkModel):
    name = STANZA
    image = STANZA_IMAGE
    container_port = STANZA_CONTAINER_PORT
    env = {
        'PROCESSORS': 'tokenize,ner',
        'NOSSPLIT': '1'
    }

    def map(self, texts):
        return map_stanza(
            texts, self.host, self.port,
            batch_size=STANZA_BATCH
        )
