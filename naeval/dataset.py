
from random import seed as seed_, sample as sample_


def sample(items, size=10000, seed=1):
    items = list(items)
    if len(items) <= size:
        return items

    seed_(seed)
    return sample_(items, size)
