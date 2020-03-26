
from ipymarkup import show_span_line_markup as show_markup_
from ipymarkup.palette import BLUE, palette

from naeval.record import Record
from naeval.span import Span
from naeval.sent import (
    sentenize,
    sent_spans
)


class Markup(Record):
    __attributes__ = ['text', 'spans']
    __annotations__ = {
        'spans': [Span]
    }

    def __init__(self, text, spans):
        self.text = text
        self.spans = spans

    @property
    def sents(self):
        for sent in sentenize(self.text):
            spans = sent_spans(sent, self.spans)
            yield Markup(sent.text, list(spans))


def show_markup(text, spans):
    show_markup_(text, spans, palette=palette(BLUE))
