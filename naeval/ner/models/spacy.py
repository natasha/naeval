
import json

from naeval.const import SPACY
from naeval.span import Span

from ..adapt import adapt_spacy
from ..markup import Markup

from .base import post, Model


SPACY_IMAGE = 'natasha/spacy-ru2'
SPACY_CONTAINER_PORT = 8080

SPACY_URL = 'http://{host}:{port}/'


class SpacyMarkup(Markup):
    label = SPACY

    @property
    def adapted(self):
        return adapt_spacy(self)


def parse_spans(data):
    for ent in data['ents']:
        yield Span(
            start=ent['start'],
            stop=ent['stop'],
            type=ent['label']
        )


def parse_spacy(text, data):
    spans = list(parse_spans(data))
    return SpacyMarkup(text, spans)


def call_spacy(text, host, port):
    url = SPACY_URL.format(
        host=host,
        port=port
    )
    payload = json.dumps(text)
    response = post(url, data=payload)
    data = response.json()
    return parse_spacy(text, data)


class SpacyModel(Model):
    name = SPACY
    image = SPACY_IMAGE
    container_port = SPACY_CONTAINER_PORT

    def __call__(self, text):
        return call_spacy(text, self.host, self.port)
