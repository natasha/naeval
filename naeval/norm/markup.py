
from naeval.span import Span
from naeval.ner.markup import (
    Markup,
    show_markup
)


class NormSpan(Span):
    __attributes__ = ['start', 'stop', 'type', 'normal']

    def __init__(self, start, stop, type, normal):
        self.start = start
        self.stop = stop
        self.type = type
        self.normal = normal

    def offset(self, delta):
        return NormSpan(
            self.start + delta,
            self.stop + delta,
            self.type, self.normal
        )


class Markup(Markup):
    __annotations__ = {
        'spans': [NormSpan]
    }
