
from naeval.const import SPACY

from ..markup import Token, Markup

from .conll import parse_conll_feats
from .base import Model


SPACY_CONTAINER_PORT = 8080
SPACY_IMAGE = 'natasha/spacy-ru2'


def parse_spacy(data):
    # {'word': 'мама', 'lemma': 'мама', 'tag': 'NOUN__Animacy=Anim|Case=Nom
    # {'word': 'мыла', 'lemma': 'мыть', 'tag': 'VERB__Aspect=Imp|Gender=Fem

    markup = Markup([])
    for item in data:
        tag = item['tag']
        pos, feats = tag.split('__', 1)
        feats = dict(parse_conll_feats(feats))
        token = Token(item['word'], pos, feats)
        markup.tokens.append(token)
    return markup


class SpacyModel(Model):
    name = SPACY
    image = SPACY_IMAGE
    container_port = SPACY_CONTAINER_PORT

    parse = staticmethod(parse_spacy)
