
from corus import load_gramru

from .markup import Token, Markup


def adapt_tokens(tokens):
    for token in tokens:
        if not token.lemma:
            # rare, social
            continue

        yield Token(
            token.text,
            token.lemma.lower(),  # Буш, Интерфакса, PROPN?
            token.pos, token.feats
        )


def load_dataset(path):
    for record in load_gramru(path):
        tokens = list(adapt_tokens(record.tokens))
        yield Markup(tokens)
