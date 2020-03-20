
from naeval.const import NATASHA
from naeval.span import Span

from ..adapt import adapt_natasha
from ..markup import Markup

from .base import post, Model


NATASHA_IMAGE = 'natasha/natasha:0.10.0'
NATASHA_CONTAINER_PORT = 8080
NATASHA_URL = 'http://{host}:{port}/'


class NatashaMatch(Span):
    __attributes__ = ['start', 'stop', 'type', 'fact']

    def __init__(self, start, stop, type, fact):
        self.start = start
        self.stop = stop
        self.type = type
        self.fact = fact


class NatashaMarkup(Markup):
    @property
    def adapted(self):
        return adapt_natasha(self)


def parse_matches(data):
    for item in data:
        type = item['type']
        fact = item['fact']
        start, stop = item['span']
        yield NatashaMatch(start, stop, type, fact)


def match_spans(matches):
    for match in matches:
        yield Span(match.start, match.stop, match.type)


def parse_natasha(text, data):
    matches = parse_matches(data)
    spans = list(match_spans(matches))
    return NatashaMarkup(text, spans)


def call_natasha(text, host, port):
    url = NATASHA_URL.format(
        host=host,
        port=port
    )
    payload = text.encode('utf8')
    response = post(
        url,
        data=payload
    )
    data = response.json()
    return parse_natasha(text, data)


class NatashaModel(Model):
    name = NATASHA
    image = NATASHA_IMAGE
    container_port = NATASHA_CONTAINER_PORT

    def __call__(self, text):
        return call_natasha(text, self.host, self.port)
