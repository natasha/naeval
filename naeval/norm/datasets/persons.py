
from corus import load_persons as load_persons_

from naeval.const import PER

from ..markup import NormSpan, Markup


def parse_spans(spans):
    for _, start, stop, value in spans:
        normal = value.lower()
        yield NormSpan(start, stop, PER, normal)


def parse_persons(record):
    spans = list(parse_spans(record.spans))
    return Markup(record.text, spans)


def load_persons(dir):
    for record in load_persons_(dir):
        yield parse_persons(record)
