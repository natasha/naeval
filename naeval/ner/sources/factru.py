
from corus import load_factru as load_factru_

from naeval.record import Record
from naeval.const import FACTRU
from naeval.span import (
    Span,
    offset_spans
)

from ..adapt import adapt_factru
from ..markup import Markup


class FactruSpan(Span):
    __attributes__ = ['id', 'type', 'start', 'stop']

    def __init__(self, id, type, start, stop):
        self.id = id
        self.type = type
        self.start = start
        self.stop = stop

    def offset(self, delta):
        return FactruSpan(
            self.id, self.type,
            self.start + delta,
            self.stop + delta
        )

    @classmethod
    def from_corus(cls, record):
        return FactruSpan(*record)


class FactruObject(Record):
    __attributes__ = ['id', 'type', 'spans']
    __annotations__ = {
        'spans': [FactruSpan]
    }

    def __init__(self, id, type, spans):
        self.id = id
        self.type = type
        self.spans = spans

    def offset(self, delta):
        spans = offset_spans(self.spans, delta)
        return FactruObject(
            self.id, self.type,
            list(spans)
        )

    @property
    def start(self):
        return min(_.start for _ in self.spans)

    @property
    def stop(self):
        return max(_.stop for _ in self.spans)

    @classmethod
    def from_corus(cls, record):
        return FactruObject(
            record.id, record.type,
            [FactruSpan.from_corus(_) for _ in record.spans]
        )


class FactruMarkup(Markup):
    __attributes__ = ['id', 'text', 'objects']
    __annotations__ = {
        'objects': [FactruObject]
    }

    label = FACTRU

    def __init__(self, id, text, objects):
        self.id = id
        self.text = text
        self.objects = objects

    @property
    def spans(self):
        for object in self.objects:
            for span in object.spans:
                label = span.type + '_' + object.id[-2:]
                yield Span(span.start, span.stop, label)
            label = object.type + '_' + object.id[-2:]
            yield Span(object.start, object.stop, label)

    @property
    def adapted(self):
        return adapt_factru(self)

    @classmethod
    def from_corus(cls, record):
        return FactruMarkup(
            record.id, record.text,
            [FactruObject.from_corus(_) for _ in record.objects]
        )


def load_factru(dir):
    for record in load_factru_(dir):
        yield FactruMarkup.from_corus(record)
