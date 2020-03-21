
from corus import load_wikiner as load_wikiner_

from naeval.tokenizer import Token

from ..bio import bio_spans
from ..adapt import adapt_wikiner
from ..markup import Markup


class WikinerMarkup(Markup):
    @property
    def adapted(self):
        return adapt_wikiner(self)


def chunk_tokens(chunks, sep=1):
    start = 0
    for chunk in chunks:
        stop = start + len(chunk)
        yield Token(start, stop, chunk)
        start = stop + sep


def parse_wikiner(record):
    chunks, tags = [], []
    for chunk, pos, tag in record.tokens:
        chunks.append(chunk)
        tags.append(tag)

    text = ' '.join(chunks)
    tokens = chunk_tokens(chunks)
    spans = list(bio_spans(tokens, tags))
    return WikinerMarkup(text, spans)


def load_wikiner(path):
    for record in load_wikiner_(path):
        yield parse_wikiner(record)
