
from collections import defaultdict

from naeval.const import SLOVNET_BERT
from naeval.chop import chop

from ..markup import Token, Markup

from .base import post, ChunkModel


SLOVNET_CONTAINER_PORT = 8080
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


def order_size(items):
    sizes = defaultdict(list)
    for index, words in enumerate(items):
        sizes[len(words)].append([index, words])

    order = []
    chunks = []
    for size in sorted(sizes):
        chunk = []
        for index, words in sizes[size]:
            order.append(index)
            chunk.append(words)
        chunks.append(chunk)
    return order, chunks


def reorder(items, order):
    items_ = [None] * len(order)
    for index, item in enumerate(items):
        items_[order[index]] = item
    return items_


def map_slovnet(items, host, port):
    chunk = chop(items, SLOVNET_CHUNK)
    for chunk in chunk:
        order, groups = order_size(chunk)
        markups = []
        for group in groups:
            markups.extend(call_slovnet(group, host, port))
        yield from reorder(markups, order)


class SlovnetBERTModel(ChunkModel):
    name = SLOVNET_BERT
    image = SLOVNET_BERT_IMAGE
    container_port = SLOVNET_CONTAINER_PORT

    def map(self, items):
        return map_slovnet(items, self.host, self.port)
