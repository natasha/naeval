
from naeval.const import SLOVNET, SLOVNET_BERT
from naeval.chop import chop

from ..markup import Token, Markup

from .base import post, ChunkModel


SLOVNET_CONTAINER_PORT = 8080
SLOVNET_IMAGE = 'natasha/slovnet-morph'
SLOVNET_BERT_IMAGE = 'natasha/slovnet-syntax-bert'
SLOVNET_URL = 'http://{host}:{port}/'
SLOVNET_CHUNK = 1000


def parse_tokens(items):
    for item in items:
        yield Token(
            item['id'], item['text'],
            item['head_id'], item['rel']
        )


def parse_slovnet(data):
    for item in data:
        tokens = list(parse_tokens(item['tokens']))
        yield Markup(tokens)


def call_slovnet(items, host, port):
    url = SLOVNET_URL.format(
        host=host,
        port=port
    )
    response = post(url, json=items)
    data = response.json()
    return parse_slovnet(data)


def map_slovnet(items, host, port):
    chunks = chop(items, SLOVNET_CHUNK)
    for chunk in chunks:
        yield from call_slovnet(chunk, host, port)


class SlovnetModel(ChunkModel):
    name = SLOVNET
    image = SLOVNET_IMAGE
    container_port = SLOVNET_CONTAINER_PORT

    def map(self, texts):
        return map_slovnet(texts, self.host, self.port)


class SlovnetBERTModel(SlovnetModel):
    name = SLOVNET_BERT
    image = SLOVNET_BERT_IMAGE
