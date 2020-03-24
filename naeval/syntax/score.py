
from naeval.record import Record
from naeval.score import Share


class Score(Record):
    __attributes__ = ['uas', 'las']

    def __init__(self, uas=None, las=None):
        if not uas:
            uas = Share()
        self.uas = uas
        if not las:
            las = Share()
        self.las = las

    def add(self, value):
        self.uas.add(value.uas)
        self.las.add(value.las)

    def reset(self):
        self.uas.reset()
        self.las.reset()


def score_tokens(preds, targets):
    score = Score()
    for pred, target in zip(preds, targets):
        score.uas.total += 1
        score.las.total += 1
        if pred.head_id == target.head_id:
            score.uas.correct += 1
            if pred.rel == target.rel:
                score.las.correct += 1
    return score


def score_markups(preds, targets):
    score = Score()
    for pred, target in zip(preds, targets):
        score.add(score_tokens(pred.tokens, target.tokens))
    return score
