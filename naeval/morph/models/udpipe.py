
from urllib.parse import quote

from naeval.const import UDPIPE

from ..markup import Token, Markup

from .conll import parse_conll_feats
from .base import get, Model


UDPIPE_CONTAINER_PORT = 8080
UDPIPE_IMAGE = 'natasha/udpipe-ru'
UDPIPE_URL = (
    'http://{host}:{port}/process'
    '?tagger&input=horizontal&data={data}'
)


def parse_udpipe(data):
    lines = data['result'].splitlines()
    # # newdoc
    # # newpar
    # # sent_id = 1
    # # text = мама мыла раму
    # 1	мама	мама	NOUN	_	Animacy=Anim|Case=Nom|Gender=Fem|Number=Sing	_	_	_	_
    # 2	мыла	мыть	VERB	_	Aspect=Imp|Gender=Fem|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Act	_	_	_	_

    markup = Markup([])
    for line in lines:
        if not line or line.startswith('#'):
            continue

        index, word, lemma, pos, _, feats, _ = line.split('\t', 6)
        feats = dict(parse_conll_feats(feats))
        markup.tokens.append(Token(word, pos, feats))
    return markup


def call_udpipe(words, host, port):
    data = ' '.join(words)
    url = UDPIPE_URL.format(
        host=host,
        port=port,
        data=quote(data)
    )
    data = get(url).json()
    return parse_udpipe(data)


class UDPipeModel(Model):
    name = UDPIPE
    image = UDPIPE_IMAGE
    container_port = UDPIPE_CONTAINER_PORT

    def __call__(self, words):
        return call_udpipe(words, self.host, self.port)
