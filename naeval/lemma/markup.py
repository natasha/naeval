
from naeval.morph.markup import (
    Token as Token_,
    Markup as Markup_,
    format_tag
)


class Token(Token_):
    __attributes__ = ['text', 'lemma', 'pos', 'feats']

    def __init__(self, text, lemma, pos, feats):
        super(Token, self).__init__(text, pos, feats)
        self.lemma = lemma


class Markup(Markup_):
    __annotations__ = {
        'tokens': [Token]
    }


def format_markup(markup, size=20):
    if not markup.tokens:
        return

    for token in markup.tokens:
        word = token.text.rjust(size)
        lemma = token.lemma.rjust(size)
        tag = format_tag(token.pos, token.feats)
        yield f'{word} {lemma} {tag}'


def show_markup(markup):
    for line in format_markup(markup):
        print(line)


def format_markup_diff(a, b, size=20):
    for a, b in zip(a.tokens, b.tokens):
        word = a.text.rjust(size)
        lemma = a.lemma.rjust(size)
        tag = format_tag(a.pos, a.feats)
        yield f'{word} {lemma} {tag}'
        if a.lemma != b.lemma:
            fill = ' ' * size
            lemma = b.lemma.rjust(size)
            yield f'{fill} {lemma}'


def show_markup_diff(a, b):
    for line in format_markup_diff(a, b):
        print(line)
