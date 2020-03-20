
from pymorphy2 import MorphAnalyzer

from corus import (
    load_simlex as load_simlex_,
    load_russe_hj as load_hj_,
    load_russe_rt as load_rt_,
    load_russe_ae as load_ae_,
    load_toloka_lrwc as load_lrwc_
)

from naeval.record import Record
from naeval.const import (
    NOUN,
    ADJ,
    VERB
)


POSES = {NOUN, ADJ, VERB}
POS_ALIASES = {'ADJF': ADJ}


class Sim(Record):
    __attributes__ = ['a', 'b', 'a_pos', 'b_pos', 'weight']

    def __init__(self, a, b, a_pos, b_pos, weight):
        self.a = a
        self.b = b
        self.a_pos = a_pos
        self.b_pos = b_pos
        self.weight = weight


def map_model(model, records, tagged):
    for record in records:
        a, b = record.a, record.b
        if tagged:
            a = add_pos(a, record.a_pos)
            b = add_pos(b, record.b_pos)

        weight = None
        if a in model and b in model:
            weight = model.sim(a, b)

        yield Sim(
            record.a, record.b,
            record.a_pos, record.b_pos,
            weight
        )


def split_pos(value):
    return value.split('_', 1)


def add_pos(word, pos):
    return '%s_%s' % (word, pos)


def get_pos(word, analyzer):
    records = analyzer.parse(word)
    for record in records:
        pos = record.tag.POS
        pos = POS_ALIASES.get(pos, pos)
        if pos in POSES:
            return pos
    return NOUN


def load_simlex(path):
    records = load_simlex_(path)
    for record in records:
        a, a_pos = split_pos(record.word1)
        b, b_pos = split_pos(record.word2)
        yield Sim(a, b, a_pos, b_pos, record.score)


def load_noun(path, load):
    records = load(path)
    for a, b, weight in records:
        yield Sim(a, b, NOUN, NOUN, weight)


def load_hj(path):
    return load_noun(path, load_hj_)


def load_rt(path):
    return load_noun(path, load_rt_)


def load_ae(paths):
    analyzer = MorphAnalyzer()
    for path in paths:
        for a, b, weight in load_ae_(path):
            a_pos = get_pos(a, analyzer)
            b_pos = get_pos(b, analyzer)
            yield Sim(a, b, a_pos, b_pos, weight)


def load_ae2(path):
    return load_noun(path, load_ae_)


def load_lrwc(path):
    for record in load_lrwc_(path):
        yield Sim(
            record.hyponym,
            record.hypernym,
            NOUN, NOUN,
            record.judgement
        )
