
from naeval.const import SLOVNET_BERT
from naeval.span import Span
from naeval.chop import chop

from ..adapt import adapt_slovnet
from ..markup import Markup

from .base import post, ChunkModel


SLOVNET_BERT_IMAGE = 'natasha/slovnet-ner-bert'
SLOVNET_CONTAINER_PORT = 8080
SLOVNET_URL = 'http://{host}:{port}/'
SLOVNET_CHUNK = 1000


class SlovnetMarkup(Markup):
    @property
    def adapted(self):
        return adapt_slovnet(self)


def parse_spans(items):
    for item in items:
        yield Span(item['start'], item['stop'], item['type'])


def parse_slovnet(data):
    for item in data:
        text = item['text']
        spans = list(parse_spans(item['spans']))
        yield SlovnetMarkup(text, spans)


def call_slovnet(texts, host, port):
    url = SLOVNET_URL.format(
        host=host,
        port=port
    )
    response = post(url, json=texts)
    data = response.json()
    return parse_slovnet(data)


def map_slovnet(texts, host, port):
    chunks = chop(texts, SLOVNET_CHUNK)
    for chunk in chunks:
        yield from call_slovnet(chunk, host, port)


class SlovnetBERTModel(ChunkModel):
    name = SLOVNET_BERT
    image = SLOVNET_BERT_IMAGE
    container_port = SLOVNET_CONTAINER_PORT

    def map(self, texts):
        return map_slovnet(texts, self.host, self.port)
