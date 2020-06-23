
from naeval.const import STANZA
from naeval.chop import chop

from ..markup import Token, Markup

from .base import post, ChunkModel


STANZA_CONTAINER_PORT = 8080
STANZA_IMAGE = 'natasha/stanza-ru'
STANZA_URL = 'http://{host}:{port}/'
STANZA_BATCH = 32


def parse_stanza(data):
    # {'id': '1',
    #  'text': 'Путин',
    #  'lemma': 'Путин',
    #  'upos': 'PROPN',
    #  'feats': 'Animacy=Anim|Case=Nom|Gender=Masc|Number=Sing',
    #  'head': 2,
    #  'deprel': 'nsubj',
    #  'misc': 'start_char=0|end_char=5'}

    for sent in data['sentences']:
        markup = Markup([])
        for item in sent:
            id = item['id']
            text = item['text']
            head_id = str(item['head'])
            rel = item['deprel']
            markup.tokens.append(Token(id, text, head_id, rel))
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


def map_deepavlov(items, host, port,
                  batch_size=STANZA_BATCH):
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
        'PROCESSORS': 'tokenize,pos,lemma,depparse',
        'PRETOKENIZED': '1',
        'NOSSPLIT': '1'
    }

    def map(self, items):
        return map_deepavlov(
            items, self.host, self.port,
            self.batch_size
        )
