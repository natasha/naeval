
from corus import load_ne5 as load_ne5_

from naeval.span import Span

from ..markup import Markup
from ..adapt import adapt_ne5


class Ne5Markup(Markup):
    @property
    def adapted(self):
        return adapt_ne5(self)


def parse_spans(spans):
    for span in spans:
        yield Span(span.start, span.stop, span.type)


def parse_ne5(record):
    spans = list(parse_spans(record.spans))
    return Ne5Markup(record.text, spans)


def load_ne5(dir):
    for record in load_ne5_(dir):
        yield parse_ne5(record)
