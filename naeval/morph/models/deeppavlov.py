
from naeval.const import DEEPPAVLOV, DEEPPAVLOV_BERT

from ..markup import Token, Markup

from .base import post, ChunkModel
from .conll import parse_conll_feats


DEEPPAVLOV_CONTAINER_PORT = 5000
DEEPPAVLOV_IMAGE = 'natasha/deeppavlov-morph-ru'
DEEPPAVLOV_BERT_IMAGE = 'natasha/deeppavlov-morph-ru-bert'
DEEPPAVLOV_URL = 'http://{host}:{port}/model'
DEEPPAVLOV_BATCH = 128
DEEPPAVLOV_BERT_BATCH = 128


def parse_deeppavlov(data, mode=DEEPPAVLOV):
    # [
    #   [
    #     "1\ta\tX\tForeign=Yes\n2\tb\tX\tForeign=Yes\n"
    #   ],
    #   [
    #     "1\ta\tX\tForeign=Yes\n"
    #   ]
    # ]

    for item in data:
        markup = Markup([])
        lines = item[0].splitlines()
        for line in lines:
            if mode == DEEPPAVLOV:
                index, word, pos, feats = line.split('\t', 3)
            elif mode == DEEPPAVLOV_BERT:
                # 1\tМинистр\tминистр\tNOUN\t_\tAnimacy=Anim|Case=Nom|Gender...
                index, word, _, pos, _, feats = line.split('\t')[:6]
            feats = dict(parse_conll_feats(feats))
            markup.tokens.append(Token(word, pos, feats))
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


def call_deeppavlov(batch, host, port, mode=DEEPPAVLOV):
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
    return parse_deeppavlov(data, mode)


def map_deepavlov(items, host, port,
                  batch_size=DEEPPAVLOV_BATCH, mode=DEEPPAVLOV):
    batches = group_chunks(items, batch_size)
    for batch in batches:
        markups = call_deeppavlov(batch, host, port, mode)
        for markup in markups:
            yield markup


class DeeppavlovModel(ChunkModel):
    name = DEEPPAVLOV
    image = DEEPPAVLOV_IMAGE
    container_port = DEEPPAVLOV_CONTAINER_PORT
    batch_size = DEEPPAVLOV_BATCH
    mode = DEEPPAVLOV

    def map(self, items):
        return map_deepavlov(
            items, self.host, self.port,
            self.batch_size, self.mode
        )


class DeeppavlovBERTModel(DeeppavlovModel):
    name = DEEPPAVLOV_BERT
    image = DEEPPAVLOV_BERT_IMAGE
    container_port = DEEPPAVLOV_CONTAINER_PORT
    batch_size = DEEPPAVLOV_BERT_BATCH
    mode = DEEPPAVLOV_BERT
