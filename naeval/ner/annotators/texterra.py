
from naeval.const import TEXTERRA
from naeval.span import Span

from ..adapt import adapt_texterra
from ..markup import Markup

from .base import post, ChunkAnnotator


TEXTERRA_IMAGE = 'natasha/texterra-russian'
TEXTERRA_CONTAINER_PORT = 8080

TEXTERRA_CHUNK = 30000
TEXTERRA_TIMEOUT = 120
# if lang is undefined may try to load eng model and fail
TEXTERRA_URL = 'http://{host}:{port}/texterra/nlp?targetType=named-entity&language=ru'


class TexterraMarkup(Markup):
    label = TEXTERRA

    @property
    def adapted(self):
        return adapt_texterra(self)


def parse_annotations(data):
    if 'named-entity' not in data:
        return

    for item in data['named-entity']:
        start = item['start']
        stop = item['end']
        type = item['value']['tag']
        yield Span(start, stop, type)


def parse(data):
    for item in data:
        text = item['text']
        annotations = item['annotations']
        spans = list(parse_annotations(annotations))
        yield TexterraMarkup(text, spans)


def call(texts, host, port, timeout):
    url = TEXTERRA_URL.format(
        host=host,
        port=port
    )
    payload = [{'text': _} for _ in texts]
    response = post(
        url,
        json=payload,
        timeout=timeout
    )
    return response.json()


def group_chunks(items, cap):
    items = iter(items)
    chunk = []
    accumulator = 0
    for item in items:
        size = len(item)
        accumulator += size
        if accumulator >= cap and chunk:
            yield chunk
            chunk = []
            accumulator = size
        chunk.append(item)
    if chunk:
        yield chunk


def map(texts, host, port, chunk_size=TEXTERRA_CHUNK, timeout=TEXTERRA_TIMEOUT):
    chunks = group_chunks(texts, chunk_size)
    for chunk in chunks:
        data = call(chunk, host, port, timeout)
        for markup in parse(data):
            yield markup


class TexterraAnnotator(ChunkAnnotator):
    name = TEXTERRA
    image = TEXTERRA_IMAGE
    container_port = TEXTERRA_CONTAINER_PORT

    def map(self, texts):
        return map(texts, self.host, self.port)
