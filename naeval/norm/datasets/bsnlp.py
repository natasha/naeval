
from corus import load_bsnlp as load_bsnlp_

from naeval.const import PER, LOC, ORG
from naeval.span import (
    filter_overlapping_spans,
    select_type_spans
)

from ..markup import Span, Markup


TYPES = {
    'PER': PER,
    'LOC': LOC,
    'ORG': ORG
}


def iter_find(text, substring):
    start = text.find(substring)
    if start < 0:
        return

    while start >= 0:
        stop = start + len(substring)
        yield start, stop
        start = text.find(substring, stop)


def find_spans(text, substrings):
    for substring in substrings:
        if not substring.normal:
            # ~4 in total
            # Евросоюза, Марокко, British Airways
            continue

        for start, stop in iter_find(text, substring.text):
            normal = substring.normal.lower()
            yield Span(
                start, stop,
                substring.type,
                normal
            )


def parse_bsnlp(record):
    spans = find_spans(record.text, record.substrings)
    spans = filter_overlapping_spans(spans)
    spans = select_type_spans(spans, TYPES)
    return Markup(record.text, list(spans))


def load_bsnlp(dir):
    for record in load_bsnlp_(dir):
        yield parse_bsnlp(record)
