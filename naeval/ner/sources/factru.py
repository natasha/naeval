
from corus import load_factru as load_factru_

from naeval.record import Record
from naeval.span import Span

from ..adapt import adapt_factru
from ..markup import Markup


OBJ = 'obj'


class FactruObject(Record):
    __attributes__ = ['id', 'type', 'spans']

    def __init__(self, id, type, spans):
        self.id = id
        self.type = type
        self.spans = spans

    @property
    def start(self):
        return min(_.start for _ in self.spans)

    @property
    def stop(self):
        return max(_.stop for _ in self.spans)


class FactruMarkup(Markup):
    __attributes__ = ['text', 'objects']

    def __init__(self, text, objects):
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


def parse_objects(record):
    for object in record.objects:
        yield FactruObject(object.id, object.type, object.spans)


def parse_factru(record):
    objects = list(parse_objects(record))
    return FactruMarkup(record.text, objects)


def load_factru(dir):
    for record in load_factru_(dir):
        yield parse_factru(record)
