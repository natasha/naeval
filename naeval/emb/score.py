
from scipy.stats import spearmanr
from sklearn.metrics import average_precision_score

from naeval.record import Record


class Score(Record):
    __attributes__ = ['count', 'total' 'value']

    def __init__(self, count=0, total=0, value=None):
        self.count = count
        self.total = total
        self.value = value


def corr(preds, targets):
    corr, p = spearmanr(preds, targets)
    return corr


def prec(preds, targets):
    # note args swaped
    return average_precision_score(targets, preds)


def score(preds, targets, metric):
    score = Score()
    pairs = zip(preds, targets)
    preds, targets = [], []
    for pred, target in pairs:
        pred, target = pred.weight, target.weight
        score.total += 1
        if pred is None or target is None:
            continue
        score.count += 1
        preds.append(pred)
        targets.append(target)
    score.value = metric(preds, targets)
    return score


def score_corr(preds, targets):
    return score(preds, targets, corr)


def score_prec(preds, targets):
    return score(preds, targets, prec)
