
from pullenti_client.client import (
    Client as PullentiClient,
    ClientError as PullentiError
)

from naeval.const import (
    PULLENTI,
    LOCALHOST, PORT,
)
from naeval.span import Span

from ..adapt import adapt_pullenti
from ..markup import Markup

from .base import (
    ModelError, ConnectionError,
    Model
)


PULLENTI_IMAGE = 'pullenti/pullenti-server:3.20.2'
PULLENTI_CONTAINER_PORT = 8080


class PullentiMarkup(Markup):
    @property
    def adapted(self):
        return adapt_pullenti(self)


def result_spans(result):
    for match in result.walk():
        start, stop = match.span
        yield Span(start, stop, match.referent.label)


def call_pullenti(client, text):
    try:
        result = client(text)
    except (PullentiError, ConnectionError) as error:
        message = str(error)
        raise ModelError(message)

    spans = list(result_spans(result))
    return PullentiMarkup(result.text, spans)


class PullentiModel(Model):
    name = PULLENTI
    image = PULLENTI_IMAGE
    container_port = PULLENTI_CONTAINER_PORT

    def __init__(self, host=LOCALHOST, port=PORT):
        super(PullentiModel, self).__init__(host, port)
        self.client = PullentiClient(host, port)

    def __call__(self, text):
        return call_pullenti(self.client, text)
