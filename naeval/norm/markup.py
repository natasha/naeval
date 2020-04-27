
from naeval.span import Span as Span
from naeval.ner.markup import (
    Markup as Markup_,
    show_markup
)


class Span(Span_):
    __attributes__ = ['start', 'stop', 'type', 'normal']

    def __init__(self, start, stop, type, normal):
        super(Span, self).__init__(start, stop, type)
        self.normal = normal

    def offset(self, delta):
        return Span(
            self.start + delta,
            self.stop + delta,
            self.type, self.normal
        )


class Markup(Markup_):
    __annotations__ = {
        'spans': [Span]
    }
