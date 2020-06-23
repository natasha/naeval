
from naeval.const import STANZA
from naeval.chop import chop

from ..markup import Token, Markup

from .base import post, ChunkModel
from .conll import parse_conll_feats


STANZA_IMAGE = 'natasha/stanza-ru'
STANZA_CONTAINER_PORT = 8080
STANZA_URL = 'http://{host}:{port}/'
STANZA_BATCH = 32


def parse_stanza(data):
    for sent in data['sentences']:
        markup = Markup([])
        for item in sent:
            word, pos = item['text'], item['upos']
            feats = dict(parse_conll_feats(item.get('feats')))
            markup.tokens.append(Token(word, pos, feats))
        yield markup


def stanza_payload(batch):
    return '\n\n'.join(
        '\t'.join(sent)
        for sent in batch
    )


def call_stanza(batch, host, port):
    url = STANZA_URL.format(
        host=host,
        port=port
    )
    payload = stanza_payload(batch)
    response = post(url, json=payload)
    data = response.json()
    return parse_stanza(data)


def map_stanza(items, host, port, batch_size=STANZA_BATCH):
    batches = chop(items, batch_size)
    for batch in batches:
        markups = call_stanza(batch, host, port)
        for markup in markups:
            yield markup


class StanzaModel(ChunkModel):
    name = STANZA
    image = STANZA_IMAGE
    container_port = STANZA_CONTAINER_PORT
    batch_size = STANZA_BATCH
    env = {
        'PROCESSORS': 'tokenize,pos',
        'PRETOKENIZED': '1',
        'NOSSPLIT': '1'
    }

    def map(self, items):
        return map_stanza(
            items, self.host, self.port,
            self.batch_size
        )
