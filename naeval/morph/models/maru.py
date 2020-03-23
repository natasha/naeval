
from naeval.const import MARU

from ..markup import Token, Markup

from .base import Model


MARU_CONTAINER_PORT = 8080
MARU_IMAGE = 'natasha/maru'

KEY_ALIASES = {
    'animacy': 'Animacy',
    'aspect': 'Aspect',
    'case': 'Case',
    'degree': 'Degree',
    'gender': 'Gender',
    'mood': 'Mood',
    'number': 'Number',
    'numform': 'NumForm',
    'person': 'Person',
    'tense': 'Tense',
    'variant': 'Variant',
    'verbform': 'VerbForm',
    'voice': 'Voice',
}
VALUE_ALIASES = {
    # 13408 NUM|NumForm=Digit
    #      |NUM|NumForm=Int
    'Int': 'Digit'
}


def parse_maru_feats(data):
    pos = data.pop('pos')
    feats = {}
    for key, value in data.items():
        key = KEY_ALIASES[key]
        value = VALUE_ALIASES.get(value, value)
        feats[key] = value
    return pos, feats


def parse_maru(data):
    markup = Markup([])
    for item in data:
        word = item['word']
        pos, feats = parse_maru_feats(item['tag'])
        markup.tokens.append(Token(word, pos, feats))
    return markup


class MaruModel(Model):
    name = MARU
    image = MARU_IMAGE
    container_port = MARU_CONTAINER_PORT

    parse = staticmethod(parse_maru)
