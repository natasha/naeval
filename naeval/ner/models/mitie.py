
from naeval.const import MITIE
from naeval.span import Span

from ..adapt import adapt_mitie
from ..markup import Markup

from .token import find_tokens
from .base import post, Model


MITIE_IMAGE = 'natasha/mitie-ner-ru'
MITIE_CONTAINER_PORT = 8080

MITIE_URL = 'http://{host}:{port}/'


class MitieMarkup(Markup):
    label = MITIE

    @property
    def adapted(self):
        return adapt_mitie(self)


def parse_spans(tokens, spans):
    for start, stop, type, weight in spans:
        start = tokens[start].start
        stop = tokens[stop - 1].stop
        yield Span(start, stop, type)


MITIE_STRIP = '\xa0\t\r\n '


def parse_mitie(text, data):
    chunks, spans = data
    tokens = list(find_tokens(chunks, text, strip=MITIE_STRIP))
    spans = list(parse_spans(tokens, spans))
    return MitieMarkup(text, spans)


def call_mitie(text, host, port):
    url = MITIE_URL.format(
        host=host,
        port=port
    )
    payload = text.encode('utf8')
    response = post(url, data=payload)
    data = response.json()
    return parse_mitie(text, data)


class MitieModel(Model):
    name = MITIE
    image = MITIE_IMAGE
    container_port = MITIE_CONTAINER_PORT

    def __call__(self, text):
        return call_mitie(text, self.host, self.port)
