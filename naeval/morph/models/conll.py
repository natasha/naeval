

def parse_conll_feats(feats):
    if feats == '_':
        return

    for pair in feats.split('|'):
        yield pair.split('=', 1)
