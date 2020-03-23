
# Procedure from https://github.com/dialogue-evaluation/morphoRuEval-2017/blob/master/evaluate.py

from naeval.score import Share


NOUN = 'NOUN'
ADV = 'ADV'
PRON = 'PRON'
DET = 'DET'
ADJ = 'ADJ'
VERB = 'VERB'
NUM = 'NUM'
PROPN = 'PROPN'

GENDER = 'Gender'
NUMBER = 'Number'
CASE = 'Case'
VARIANT = 'Variant'
DEGREE = 'Degree'
VERBFORM = 'VerbForm'
NUMFORM = 'Form'
MOOD = 'Mood'
TENSE = 'Tense'

# Tense
PRES = 'Pres'
FUT = 'Fut'
NOTPAST = 'Notpast'

# Variant
SHORT = 'Short'
BREV = 'Brev'

DOUBT_ADV = {'как', 'когда', 'пока', 'так', 'где'}
EVAL_POS = {NOUN, PRON, DET, ADJ, VERB, NUM}
EVAL_FEATS = {
    NOUN: {GENDER, NUMBER, CASE},

    # иракские   ADJ|Case=Nom|Degree=Pos|Number=Plur
    #          ! ADJ|Case=Nom|Degree=Pos|Number=Plur|Variant=Full
    ADJ: {GENDER, NUMBER, CASE, DEGREE},  # , VARIANT
    PRON: {GENDER, NUMBER, CASE},
    DET: {GENDER, NUMBER, CASE},
    VERB: {GENDER, NUMBER, VERBFORM, MOOD, TENSE},
    ADV: {DEGREE},
    NUM: {GENDER, NUMBER, CASE, NUMFORM},
}


def normalize_pos(pos):
    if pos == PROPN:
        return NOUN
    return pos


def normalize_feats(pos, feats):
    normal = {}

    for key in EVAL_FEATS[pos]:
        if key in feats:
            normal[key] = feats[key]

    if pos == VERB and normal.get(TENSE) in (PRES, FUT):
        normal[TENSE] = NOTPAST

    if normal.get(VARIANT) == SHORT:
        normal[VARIANT] = BREV

    return normal


def do_score(target):
    pos = normalize_pos(target.pos)
    if pos in EVAL_POS:
        return True
    if pos == ADV and target.text.lower() not in DOUBT_ADV:
        return True
    return False


def do_match(pred, target):
    pred_pos = normalize_pos(pred.pos)
    target_pos = normalize_pos(target.pos)

    if target_pos != pred_pos:
        return False

    target_feats = normalize_feats(target_pos, target.feats)
    pred_feats = normalize_feats(pred_pos, pred.feats)

    for key in target_feats:
        if target_feats[key] != pred_feats.get(key):
            return False

    return True


def score_tokens(preds, targets):
    accuracy = Share()
    for pred, target in zip(preds, targets):
        if do_score(target):
            accuracy.total += 1
            if do_match(pred, target):
                accuracy.correct += 1
    return accuracy


def score_markups(preds, targets):
    accuracy = Share()
    for pred, target in zip(preds, targets):
        accuracy.add(score_tokens(pred.tokens, target.tokens))
    return accuracy
