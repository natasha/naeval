
from corus import load_gramru

from .markup import Token, Markup


def adapt_tokens(tokens):
    for token in tokens:
        yield Token(token.id, token.text, token.head_id, token.rel)


def load_dataset(path):
    for record in load_gramru(path):
        tokens = list(adapt_tokens(record.tokens))
        yield Markup(tokens)
