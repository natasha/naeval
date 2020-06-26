
from naeval.score import F1


def score_partitions(preds, targets):
    score = F1()
    for pred, target in zip(preds, targets):
        pred = set(pred.splits)
        target = set(target.splits)
        intersection = len(pred & target)
        score.prec.total += len(pred)
        score.prec.correct += intersection
        score.recall.total += len(target)
        score.recall.correct += intersection
    return score
