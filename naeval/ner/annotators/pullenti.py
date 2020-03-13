
from pullenti_client import Client as PullentiClient
from pullenti_client.result import (
    Span as PullentiSpan_,
    Match as PullentiMatch_,
    Result as PullentiMarkup_,
)

from naeval.const import PULLENTI
from naeval.record import Record
from naeval.span import Span

from ..adapt import adapt_pullenti
from ..markup import Markup

from .base import ChunkAnnotator


PULLENTI_IMAGE = 'pullenti/pullenti-server:3.17'
PULLENTI_CONTAINER_PORT = 8080


class PullentiSpan(PullentiSpan_, Span):
    def offset(self, delta):
        return PullentiSpan(
            self.start + delta,
            self.stop + delta
        )

    @classmethod
    def from_client(cls, span):
        return PullentiSpan(span.start, span.stop)


class PullentiMatch(PullentiMatch_, Record):
    def offset(self, delta):
        return PullentiMatch(
            self.referent,
            self.span.offset(delta),
            [_.offset(delta) for _ in self.children]
        )

    @property
    def start(self):
        return self.span.start

    @property
    def stop(self):
        return self.span.stop

    @property
    def depth(self):
        if not self.children:
            return 1
        else:
            return 1 + max(_.depth for _ in self.children)

    @classmethod
    def from_client(cls, match):
        return PullentiMatch(
            match.referent,
            PullentiSpan.from_client(match.span),
            [PullentiMatch.from_client(_) for _ in match.children]
        )


class PullentiMarkup(PullentiMarkup_, Markup):
    label = PULLENTI

    @property
    def spans(self):
        for match in self.walk():
            start, stop = match.span
            yield Span(start, stop, match.referent.label)

    @property
    def adapted(self):
        return adapt_pullenti(self)

    @property
    def depth(self):
        if not self.matches:
            return
        return max(_.depth for _ in self.matches)

    @classmethod
    def from_client(cls, result):
        return PullentiMarkup(
            result.text,
            [PullentiMatch.from_client(_) for _ in result.matches]
        )

    @classmethod
    def from_json(cls, data):
        result = PullentiMarkup_.from_json(data)
        return cls.from_client(result)


def map(texts, host, port):
    client = PullentiClient(host, port)
    for text in texts:
        result = client(text)
        yield PullentiMarkup.from_client(result)


class PullentiAnnotator(ChunkAnnotator):
    name = PULLENTI

    def map(self, texts):
        return map(texts, self.host, self.port)
