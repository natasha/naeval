
from naeval.const import SPACY

from ..markup import Token, Markup

from .base import Model


SPACY_CONTAINER_PORT = 8080
SPACY_IMAGE = 'natasha/spacy-ru2'

ROOT_ID = '0'
ROOT = 'root'


def parse_spacy(data):
    # {'id': 0, 'word': 'Министр', ... 'head': 0, 'dep': 'ROOT'}
    # {'id': 8, 'word': 'общественн' ... 'head': 22, 'dep': 'amod'}

    markup = Markup([])
    ids = {}
    for index, item in enumerate(data, 1):
        id, text, head_id, rel = item['id'], item['word'], item['head'], item['dep']
        ids[id] = str(index)
        markup.tokens.append(Token(id, text, head_id, rel))

    for token in markup.tokens:
        if token.head_id == token.id:
            token.head_id = ROOT_ID
            token.rel = ROOT
        else:
            token.head_id = ids[token.head_id]
        token.id = ids[token.id]

    return markup


class SpacyModel(Model):
    name = SPACY
    image = SPACY_IMAGE
    container_port = SPACY_CONTAINER_PORT

    parse = staticmethod(parse_spacy)
