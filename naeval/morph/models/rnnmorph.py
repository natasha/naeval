
from naeval.const import RNNMORPH

from ..markup import Token, Markup

from .conll import parse_conll_feats
from .base import Model


RNNMORPH_CONTAINER_PORT = 8080
RNNMORPH_IMAGE = 'natasha/rnnmorph'


def parse_rnnmorph(data):
    markup = Markup([])
    for item in data:
        word, pos = item['word'], item['pos']
        feats = dict(parse_conll_feats(item['tag']))
        markup.tokens.append(Token(word, pos, feats))
    return markup


class RNNMorphModel(Model):
    name = RNNMORPH
    image = RNNMORPH_IMAGE
    container_port = RNNMORPH_CONTAINER_PORT

    parse = staticmethod(parse_rnnmorph)
