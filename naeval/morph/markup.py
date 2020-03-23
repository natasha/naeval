
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

    @property
    def tags(self):
        return [format_tag(_.pos, _.feats) for _ in self.tokens]


def format_tag(pos, feats):
    if not feats:
        return pos

    feats = '|'.join(
        '%s=%s' % (_, feats[_])
        for _ in sorted(feats)
    )
    return f'{pos}|{feats}'


def format_markup(markup, size=20):
    words, tags = markup.words, markup.tags
    if not words:
        return

    for word, tag in zip(words, tags):
        word = word.rjust(size)
        yield f'{word} {tag}'


def show_markup(markup):
    for line in format_markup(markup):
        print(line)


def format_markup_diff(a, b, size=20):
    from .score import do_score, do_match

    words = a.words
    if not words:
        return

    assert words == b.words

    for word, a_token, b_token in zip(words, a.tokens, b.tokens):
        word = word.rjust(size)
        a_tag = format_tag(a_token.pos, a_token.feats)
        yield f'{word}   {a_tag}'
        if a_token != b_token:
            word = ' ' * size
            sep = '?'
            if do_score(a_token) and not do_match(a_token, b_token):
                sep = '!'
            b_tag = format_tag(b_token.pos, b_token.feats)
            yield f'{word} {sep} {b_tag}'


def show_markup_diff(a, b):
    for line in format_markup_diff(a, b):
        print(line)
