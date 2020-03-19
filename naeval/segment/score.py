
from naeval.record import Record


class Score(Record):
    __attributes__ = ['prec', 'recall']

    def __init__(self, prec=0, recall=0):
        self.prec = prec
        self.recall = recall


def score_partitions(preds, targets):
    errors = Score()
    for pred, target in zip(preds, targets):
        pred = set(pred.bounds)
        target = set(target.bounds)
        errors.prec += len(pred - target)
        errors.recall += len(target - pred)
    return errors
