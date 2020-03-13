
from functools import lru_cache

from razdel import tokenize as tokenize__

from .record import Record


class Token(Record):
    __attributes__ = ['start', 'stop', 'text']

    def __init__(self, start, stop, text):
        self.start = start
        self.stop = stop
        self.text = text


def tokenize_(text):
    for token in tokenize__(text):
        yield Token(
            token.start,
            token.stop,
            token.text
        )


@lru_cache(maxsize=10000)
def tokenize(text):
    return list(tokenize_(text))
