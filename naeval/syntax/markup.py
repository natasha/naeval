
from ipymarkup.dep import show_dep_markup as show_markup_

from naeval.record import Record


class Token(Record):
    __attributes__ = ['id', 'text', 'head_id', 'rel']

    def __init__(self, id, text, head_id, rel):
        self.id = id
        self.text = text
        self.head_id = head_id
        self.rel = rel


class Markup(Record):
    __attributes__ = ['tokens']
    __annotations__ = {
        'tokens': [Token]
    }

    def __init__(self, tokens):
        self.tokens = tokens

    @property
    def words(self):
        return [_.text for _ in self.tokens]


def token_deps(tokens):
    for token in tokens:
        id = int(token.id)
        head_id = int(token.head_id)
        rel = token.rel
        id = id - 1
        if head_id == 0:  # skip root=0
            continue
        head_id = head_id - 1
        yield head_id, id, rel


def show_markup(markup):
    deps = token_deps(markup.tokens)
    show_markup_(markup.words, deps)
