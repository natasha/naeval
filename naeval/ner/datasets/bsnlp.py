
from corus import load_bsnlp as load_bsnlp_

from naeval.span import (
    Span,
    filter_overlapping_spans
)

from ..markup import Markup
from ..adapt import adapt_bsnlp


class BsnlpMarkup(Markup):
    @property
    def adapted(self):
        return adapt_bsnlp(self)


def iter_find(text, substring):
    start = text.find(substring)
    if start < 0:
        # For ru just 3 substrings missing:
        #   "Северный поток – 2"
        #   Евгений Хвостик
        #   Тереза Мэй
        return

    while start >= 0:
        stop = start + len(substring)
        yield start, stop
        start = text.find(substring, stop)


def find_spans(text, substrings):
    for substring in substrings:
        for start, stop in iter_find(text, substring.text):
            yield Span(start, stop, substring.type)


def parse_bsnlp(record):
    spans = find_spans(record.text, record.substrings)
    spans = list(filter_overlapping_spans(spans))
    return BsnlpMarkup(record.text, spans)


def load_bsnlp(dir):
    for record in load_bsnlp_(dir):
        yield parse_bsnlp(record)
