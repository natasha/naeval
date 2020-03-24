
from naeval.const import DEEPPAVLOV_BERT

from ..markup import Token, Markup

from .base import post, ChunkModel


DEEPPAVLOV_CONTAINER_PORT = 5000
DEEPPAVLOV_BERT_IMAGE = 'natasha/deeppavlov-syntax-ru-bert'
DEEPPAVLOV_URL = 'http://{host}:{port}/model'
DEEPPAVLOV_BERT_BATCH = 256


def parse_deeppavlov(data):
    # [
    #   [
    #     "1\ta\t_\t_\t_\t_\t0\troot\t_\t_\n2\tb\t_\t_\t_\t_\t1\tflat:name\t_\t_\n"
    #   ],
    #   [
    #     "1\ta\t_\t_\t_\t_\t0\tcc\t_\t_\n"
    #   ]
    # ]

    for item in data:
        markup = Markup([])
        lines = item[0].splitlines()
        for line in lines:
            id, text, _, _, _, _, head_id, rel, _, _ = line.split('\t')
            markup.tokens.append(Token(id, text, head_id, rel))
        yield markup


def group_chunks(items, size):
    buffer = []
    for item in items:
        buffer.append(item)
        if len(buffer) >= size:
            yield buffer
            buffer = []
    if buffer:
        yield buffer


def call_deeppavlov(batch, host, port):
    # {
    #   "x": [
    #     ["a", "b"],
    #     ["a"]
    #   ]
    # }

    url = DEEPPAVLOV_URL.format(
        host=host,
        port=port
    )
    payload = {'x': batch}
    response = post(
        url,
        json=payload
    )
    data = response.json()
    return parse_deeppavlov(data)


def map_deepavlov(items, host, port,
                  batch_size=DEEPPAVLOV_BERT_BATCH):
    batches = group_chunks(items, batch_size)
    for batch in batches:
        markups = call_deeppavlov(batch, host, port)
        for markup in markups:
            yield markup


class DeeppavlovBERTModel(ChunkModel):
    name = DEEPPAVLOV_BERT
    image = DEEPPAVLOV_BERT_IMAGE
    container_port = DEEPPAVLOV_CONTAINER_PORT

    def map(self, items):
        return map_deepavlov(
            items, self.host, self.port,
            DEEPPAVLOV_BERT_BATCH
        )
