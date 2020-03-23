
from naeval.const import DEEPPAVLOV, DEEPPAVLOV_BERT

from ..markup import Token, Markup

from .base import Model
from .conll import parse_conll_feats


DEEPPAVLOV_CONTAINER_PORT = 8080
DEEPPAVLOV_IMAGE = 'natasha/deeppavlov-morph-ru'
DEEPPAVLOV_BERT_IMAGE = 'natasha/deeppavlov-morph-ru-bert'


def parse_deeppavlov(data):
    markup = Markup([])
    for content in data:
        lines = content.splitlines()
        for line in lines:
            index, word, pos, feats = line.split('\t', 3)
            feats = dict(parse_conll_feats(feats))
            markup.tokens.append(Token(word, pos, feats))
    return markup


class DeeppavlovModel(Model):
    name = DEEPPAVLOV
    image = DEEPPAVLOV_IMAGE
    port = DEEPPAVLOV_CONTAINER_PORT

    parse = staticmethod(parse_deeppavlov)


class DeeppavlovBERTModel(DeeppavlovModel):
    name = DEEPPAVLOV_BERT
    image = DEEPPAVLOV_BERT_IMAGE
    port = DEEPPAVLOV_CONTAINER_PORT
