
import re
import logging
from time import time
from contextlib import contextmanager

from naeval.record import Record

from .substring import (
    Substring,
    find_substrings
)


def labeled(label):
    def decorator(item):
        item.label = label
        return item
    return decorator


class Timing(Record):
    __attributes__ = ['model']

    def __init__(self, model):
        self.model = model
        self.time = 0

    def __call__(self, *args):
        start = time()
        result = list(self.model(*args))
        self.time += (time() - start)
        return result

    def reset(self):
        self.time = 0


#######
#
#   SENTENIZE
#
#######


DOT = re.compile(r'([.?!…])\s+')


def re_split(text):
    previous = 0
    for match in DOT.finditer(text):
        delimiter = match.group(1)
        start = match.start()
        yield text[previous:start] + delimiter
        previous = match.end()
    if previous < len(text):
        yield text[previous:]


@labeled('re.split([.?!…])')
def re_sentenize(text):
    chunks = re_split(text)
    return find_substrings(chunks, text)


@contextmanager
def no_logger(logger):
    logger.disabled = True
    try:
        yield
    finally:
        logger.disabled = False


LOGGER = logging.getLogger()


@labeled('deeppavlov/rusenttokenize')
def deeppavlov_sentenize(text):
    from rusenttokenize import ru_sent_tokenize

    with no_logger(LOGGER):
        chunks = ru_sent_tokenize(text)
    return find_substrings(chunks, text)


@labeled('nltk.sent_tokenize')
def nltk_sentenize(text):
    from nltk import sent_tokenize

    chunks = sent_tokenize(text, 'russian')
    return find_substrings(chunks, text)


@labeled('segtok.split_single')
def segtok_sentenize(text):
    # pip install segtok
    from segtok.segmenter import split_single

    chunks = split_single(text)
    return find_substrings(chunks, text)


class MosesSentenizer:
    label = 'mosestokenizer'

    def __init__(self):
        from mosestokenizer import MosesSentenceSplitter

        self.splitter = MosesSentenceSplitter('ru')

    def __call__(self, text):
        if not text:
            # prevent AssertionError: blank lines are not allowed
            return []

        chunks = self.splitter([text])
        return find_substrings(chunks, text)


def adapt_razdel(records):
    for record in records:
        yield Substring(record.start, record.stop, record.text)


@labeled('razdel.sentenize')
def razdel_sentenize(text):
    from razdel import sentenize

    sents = sentenize(text)
    return adapt_razdel(sents)


##########
#
#   TOKENIZE
#
########


TOKEN = re.compile(r'([^\W\d]+|\d+|[^\w\s])')


@labeled('re.findall(\w+|\d+|\p+)')
def re_tokenize(text):
    chunks = TOKEN.findall(text)
    return find_substrings(chunks, text)


@labeled('nltk.word_tokenize')
def nltk_tokenize(text):
    from nltk.tokenize import word_tokenize

    chunks = word_tokenize(text, 'russian')
    return find_substrings(chunks, text)


class SpacyTokenizer:
    label = 'spacy'

    def __init__(self):
        from spacy.lang.ru import Russian

        self.nlp = Russian()

    def __call__(self, text):
        doc = self.nlp(text)
        chunks = (token.text for token in doc)
        return find_substrings(chunks, text)


class TimofeevTokenizer:
    label = 'aatimofeev/spacy_russian_tokenizer'

    def __init__(self):
        from spacy.lang.ru import Russian
        from spacy_russian_tokenizer import (
            RussianTokenizer,
            MERGE_PATTERNS,
            SYNTAGRUS_RARE_CASES
        )

        self.nlp = Russian()
        self.nlp.add_pipe(
            RussianTokenizer(self.nlp, MERGE_PATTERNS + SYNTAGRUS_RARE_CASES),
            name='russian_tokenizer'
        )

    def __call__(self, text):
        doc = self.nlp(text)
        chunks = (token.text for token in doc)
        return find_substrings(chunks, text)


def parse_mystem(data):
    # {'analysis': [], 'text': 'Mystem'},
    #  {'text': ' — '},
    #  {'analysis': [{'lex': 'консольный'}], 'text': 'консольная'},
    #  {'text': ' '},
    #  {'analysis': [{'lex': 'программа'}], 'text': 'программа'},
    #  {'text': '\n'}]

    for item in data:
        text = item['text'].strip()
        if text:
            yield text


class MystemTokenizer:
    label = 'mystem'

    def __init__(self):
        from pymystem3 import Mystem

        self.analyzer = Mystem(
            grammar_info=False,
            entire_input=True,
            disambiguation=False,
            weight=False
        )

    def __call__(self, text):
        data = self.analyzer.analyze(text)
        chunks = parse_mystem(data)
        return find_substrings(chunks, text)


class MosesTokenizer:
    label = 'mosestokenizer'

    def __init__(self):
        from mosestokenizer import MosesTokenizer

        self.tokenizer = MosesTokenizer('ru')
        # disable
        self.tokenizer.argv.append('-no-escape')  # " -> &quot;
        self.tokenizer.argv.remove('-a')  # - -> @-@
        self.tokenizer.restart()

    def __call__(self, text):
        chunks = self.tokenizer(text)
        return find_substrings(chunks, text)


@labeled('segtok.word_tokenize')
def segtok_tokenize(text):
    from segtok.tokenizer import word_tokenizer

    chunks = word_tokenizer(text)
    return find_substrings(chunks, text)


@labeled('razdel.tokenize')
def razdel_tokenize(text):
    from razdel import tokenize

    sents = tokenize(text)
    return adapt_razdel(sents)


class KozievTokenizer:
    label = 'koziev/rutokenizer'

    def __init__(self):
        import rutokenizer

        self.tokenizer = rutokenizer.Tokenizer()
        self.tokenizer.load()

    def __call__(self, text):
        chunks = self.tokenizer.tokenize(text)
        return find_substrings(chunks, text)
