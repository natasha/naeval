
from collections import defaultdict

from naeval.const import PER, LOC, ORG
from naeval.tokenizer import tokenize
from naeval.span import select_type_spans
from naeval.score import F1

from .bio import (
    I,
    spans_io,
    parse_bio
)


TYPES = [PER, ORG, LOC]


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
