

def parse_conll_feats(feats):
    if not feats or feats == '_':
        return

    for pair in feats.split('|'):
        yield pair.split('=', 1)
