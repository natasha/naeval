
from corus import load_ne5 as load_ne5_

from naeval.const import NE5
from naeval.span import Span

from ..markup import Markup
from ..adapt import adapt_ne5


class Ne5Span(Span):
    __attributes__ = ['index', 'type', 'start', 'stop', 'text']

    def __init__(self, index, type, start, stop, text):
        self.index = index
        self.type = type
        self.start = start
        self.stop = stop
        self.text = text

    def offset(self, delta):
        return Ne5Span(
            self.index, self.type,
            self.start + delta,
            self.stop + delta,
            self.text
        )

    @classmethod
    def from_corus(cls, record):
        return Ne5Span(*record)


class Ne5Markup(Markup):
    __attributes__ = ['id', 'text', 'spans']
    __annotations__ = {
        'spans': [Ne5Span]
    }

    label = NE5

    def __init__(self, id, text, spans):
        self.id = id
        self.text = text
        self.spans = spans

    @property
    def adapted(self):
        return adapt_ne5(self)

    @classmethod
    def from_corus(cls, record):
        return Ne5Markup(
            record.id, record.text,
            [Ne5Span.from_corus(_) for _ in record.spans]
        )


def load_ne5(dir):
    for record in load_ne5_(dir):
        yield Ne5Markup.from_corus(record)
