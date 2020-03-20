
from naeval.record import Record


class Mean(Record):
    __attributes__ = ['sum', 'count']

    def __init__(self, sum=0, count=0):
        self.sum = sum
        self.count = count

    def add(self, value):
        self.sum += value
        self.count += 1

    @property
    def value(self):
        return self.sum / self.count

    def reset(self):
        self.sum = 0
        self.count = 0


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
