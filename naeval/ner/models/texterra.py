
from naeval.const import TEXTERRA
from naeval.span import Span

from ..adapt import adapt_texterra
from ..markup import Markup

from .base import post, ChunkModel


TEXTERRA_IMAGE = 'natasha/texterra-russian'
TEXTERRA_CONTAINER_PORT = 8080

TEXTERRA_CHUNK = 10000  # ~2x faster then without chunking, ~1.7Gb RAM
TEXTERRA_TIMEOUT = 120  # wait on startup
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


def parse_texterra(data):
    for item in data:
        text = item['text']
        annotations = item['annotations']
        spans = list(parse_annotations(annotations))
        yield TexterraMarkup(text, spans)


def call_texterra(texts, host, port, timeout):
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
    data = response.json()
    return parse_texterra(data)


def group_chunks(items, cap):
    chunk = []
    accumulator = 0
    for item in items:
        size = len(item)
        accumulator += size
        if accumulator >= cap and chunk:
            yield chunk
            chunk = [item]
            accumulator = size
        else:
            chunk.append(item)
    if chunk:
        yield chunk


def map_texterra(texts, host, port,
                 chunk_size=TEXTERRA_CHUNK, timeout=TEXTERRA_TIMEOUT):
    chunks = group_chunks(texts, chunk_size)
    for chunk in chunks:
        markups = call_texterra(chunk, host, port, timeout)
        for markup in markups:
            yield markup


class TexterraModel(ChunkModel):
    name = TEXTERRA
    image = TEXTERRA_IMAGE
    container_port = TEXTERRA_CONTAINER_PORT

    def map(self, texts):
        return map_texterra(texts, self.host, self.port)
