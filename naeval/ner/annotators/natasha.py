
from naeval.const import NATASHA
from naeval.span import Span

from ..adapt import adapt_natasha
from ..markup import Markup

from .base import post, Annotator


NATASHA_IMAGE = 'natasha/natasha:0.10.0'
NATASHA_CONTAINER_PORT = 8080
NATASHA_URL = 'http://{host}:{port}/'


class NatashaMatch(Span):
    __attributes__ = ['start', 'stop', 'type', 'fact']
    __annotations__ = {
        'start': int,
        'stop': int,
        'fact': dict
    }

    def __init__(self, start, stop, type, fact):
        self.start = start
        self.stop = stop
        self.type = type
        self.fact = fact

    def offset(self, delta):
        return NatashaMatch(
            self.start + delta,
            self.stop + delta,
            self.type,
            self.fact
        )


class NatashaMarkup(Markup):
    __attributes__ = ['text', 'matches']
    __annotations__ = {
        'matches': [NatashaMatch]
    }

    label = NATASHA

    def __init__(self, text, matches):
        self.text = text
        self.matches = matches

    @property
    def spans(self):
        for match in self.matches:
            yield Span(match.start, match.stop, match.type)

    @property
    def adapted(self):
        return adapt_natasha(self)


def parse_matches(data):
    for item in data:
        type = item['type']
        fact = item['fact']
        start, stop = item['span']
        yield NatashaMatch(start, stop, type, fact)


def parse(text, data):
    matches = list(parse_matches(data))
    return NatashaMarkup(text, matches)


def call(text, host, port):
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
    return parse(text, data)


class NatashaAnnotator(Annotator):
    name = NATASHA

    def __call__(self, text):
        return call(text, self.host, self.port)
