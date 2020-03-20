
from naeval.const import TOMITA, PER
from naeval.record import Record
from naeval.io import parse_xml
from naeval.span import Span

from ..adapt import adapt_tomita
from ..markup import Markup

from .base import Model, post


TOMITA_IMAGE = 'natasha/tomita-algfio'
TOMITA_CONTAINER_PORT = 8080
TOMITA_URL = 'http://{host}:{port}/'


class TomitaFact(Record):
    __attributes__ = [
        'start', 'stop',
        'first', 'last', 'middle', 'known_surname'
    ]

    def __init__(self, start, stop,
                 first, last, middle, known_surname):
        self.start = start
        self.stop = stop
        self.first = first
        self.last = last
        self.middle = middle
        self.known_surname = known_surname


class TomitaMarkup(Markup):
    @property
    def adapted(self):
        return adapt_tomita(self)


def parse_facts(xml):
    if xml is None:
        return

    for item in xml.findall('Person'):
        start = int(item.get('pos'))
        size = int(item.get('len'))
        stop = start + size
        last = item.find('Name_Surname')
        if last is not None:
            last = last.get('val') or None
        first = item.find('Name_FirstName')
        if first is not None:
            first = first.get('val')
        middle = item.find('Name_Patronymic')
        if middle is not None:
            middle = middle.get('val')
        known_surname = item.find('Name_SurnameIsDictionary')
        if known_surname is not None:
            known_surname = int(known_surname.get('val'))
        known_surname = bool(known_surname)
        yield TomitaFact(
            start, stop,
            first, last, middle, known_surname
        )


def fact_spans(facts):
    for fact in facts:
        yield Span(fact.start, fact.stop, PER)


def parse_tomita(text, xml):
    assert xml.tag == 'document', xml.tag
    facts = xml.find('facts')
    facts = parse_facts(facts)
    spans = list(fact_spans(facts))
    return TomitaMarkup(text, spans)


def call_tomita(text, host, port):
    url = TOMITA_URL.format(
        host=host,
        port=port
    )
    payload = text.encode('utf8')
    response = post(url, data=payload)
    xml = parse_xml(response.text)
    return parse_tomita(text, xml)


class TomitaModel(Model):
    name = TOMITA
    image = TOMITA_IMAGE
    container_port = TOMITA_CONTAINER_PORT

    def __call__(self, text):
        return call_tomita(text, self.host, self.port)
