
from naeval.const import RUPOSTAGGER

from ..markup import Token, Markup

from .conll import parse_conll_feats
from .base import Model


RUPOSTAGGER_CONTAINER_PORT = 8080
RUPOSTAGGER_IMAGE = 'natasha/rupostagger'


def parse_label(label):
    if '|' not in label:
        return label, {}

    pos, feats = label.split('|', 1)
    feats = dict(parse_conll_feats(feats))
    return pos, feats


def parse_rupostagger(data):
    markup = Markup([])
    for item in data:
        word, label = item['word'], item['label']
        pos, feats = parse_label(label)
        markup.tokens.append(Token(word, pos, feats))
    return markup


class RuPosTaggerModel(Model):
    name = RUPOSTAGGER
    image = RUPOSTAGGER_IMAGE
    container_port = RUPOSTAGGER_CONTAINER_PORT

    parse = staticmethod(parse_rupostagger)
