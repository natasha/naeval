
from corus import load_gareev as load_gareev_

from naeval.tokenizer import Token

from ..bio import bio_spans
from ..markup import Markup
from ..adapt import adapt_gareev


class GareevMarkup(Markup):
    @property
    def adapted(self):
        return adapt_gareev(self)


def chunk_tokens(chunks, sep=1):
    start = 0
    for chunk in chunks:
        stop = start + len(chunk)
        yield Token(start, stop, chunk)
        start = stop + sep


def parse_gareev(record):
    chunks, tags = [], []
    for chunk, tag in record.tokens:
        chunks.append(chunk)
        tags.append(tag)

    text = ' '.join(chunks)
    tokens = chunk_tokens(chunks)
    spans = list(bio_spans(tokens, tags))
    return GareevMarkup(text, spans)


def load_gareev(dir):
    for record in load_gareev_(dir):
        yield parse_gareev(record)
