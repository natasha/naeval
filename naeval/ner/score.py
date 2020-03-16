
from collections import defaultdict

from naeval.const import PER, LOC, ORG
from naeval.record import Record
from naeval.tokenizer import tokenize
from naeval.span import select_type_spans

from .bio import (
    I,
    spans_io,
    parse_bio
)


TYPES = [PER, ORG, LOC]


class Share(Record):
    __attributes__ = ['correct', 'total']

    def __init__(self, correct=0, total=0):
        self.correct = correct
        self.total = total

    def add(self, other):
        self.correct += other.correct
        self.total += other.total

    @property
    def value(self):
        if not self.total:
            return 0
        return self.correct / self.total

    def reset(self):
        self.correct = 0
        self.total = 0


class F1(Record):
    __attributes__ = ['prec', 'recall']

    def __init__(self, prec=None, recall=None):
        if not prec:
            prec = Share()
        self.prec = prec
        if not recall:
            recall = Share()
        self.recall = recall

    def add(self, other):
        self.prec.add(other.prec)
        self.recall.add(other.recall)

    @property
    def value(self):
        prec = self.prec.value
        recall = self.recall.value
        if not prec + recall:
            return 0
        return 2 * prec * recall / (prec + recall)

    def reset(self):
        self.prec.reset()
        self.recall.reset()


def tag_f1(tokens, pred, target, type):
    spans = list(select_type_spans(pred, type))
    preds = list(spans_io(tokens, spans))
    spans = list(select_type_spans(target, type))
    targets = list(spans_io(tokens, spans))
    score = F1()
    for pred, target in zip(preds, targets):
        pred, _ = parse_bio(pred)
        target, _ = parse_bio(target)
        if pred == I:
            score.prec.total += 1
            if target == I:
                score.prec.correct += 1
        if target == I:
            score.recall.total += 1
            if pred == I:
                score.recall.correct += 1
    return score


def score_markup(pred, target, types=TYPES):
    tokens = list(tokenize(pred.text))
    for type in types:
        score = tag_f1(tokens, pred.spans, target.spans, type)
        yield type, score


def score_markups(preds, targets, types=TYPES):
    scores = defaultdict(F1)
    for pred, target in zip(preds, targets):
        for type, score in score_markup(pred, target, types):
            scores[type].add(score)
    return dict(scores)
