
from naeval.record import Record


class Token(Record):
    __attributes__ = ['text', 'pos', 'feats']

    def __init__(self, text, pos, feats):
        self.text = text
        self.pos = pos
        self.feats = feats


class Markup(Record):
    __attributes__ = ['tokens']
    __annotations__ = {
        'tokens': [Token]
    }

    def __init__(self, tokens):
        self.tokens = tokens

    @property
    def words(self):
        return [_.text for _ in self.tokens]


def format_tag(pos, feats):
    if not feats:
        return pos

    feats = '|'.join(
        '%s=%s' % (_, feats[_])
        for _ in sorted(feats)
    )
    return f'{pos}|{feats}'


def format_markup(markup, size=20):
    if not markup.tokens:
        return

    for token in markup.tokens:
        word = token.text.rjust(size)
        tag = format_tag(token.pos, token.feats)
        yield f'{word} {tag}'


def show_markup(markup):
    for line in format_markup(markup):
        print(line)


def format_markup_diff(a, b, size=20):
    from .score import do_score, do_match

    for a, b in zip(a.tokens, b.tokens):
        word = a.text.rjust(size)
        a_tag = format_tag(a.pos, a.feats)
        yield f'{word}   {a_tag}'
        if a != b:
            fill = ' ' * size
            sep = '?'
            if do_score(a) and not do_match(a, b):
                sep = '!'
            b_tag = format_tag(b.pos, b.feats)
            yield f'{fill} {sep} {b_tag}'


def show_markup_diff(a, b):
    for line in format_markup_diff(a, b):
        print(line)
