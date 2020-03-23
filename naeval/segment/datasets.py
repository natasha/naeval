
import re

from corus import load_corpora  # noqa
from corus import load_ud_syntag as load_syntag  # noqa
from corus import load_morphoru_gicrya as load_gicrya  # noqa
from corus import load_morphoru_rnc as load_rnc  # noqa

from .substring import find_substrings
from .partition import Partition


def is_bib(text):
    # Lot of these things in Corpora:
    # Astronomical Journal. — 1987. — С. 178—188.
    if re.search(r'— С. \d', text):
        return True

    # Калашниковой. – М.: Центрполиграф
    if re.search(r'[-—–]\s*(М|M|СПб)\.[:,]', text):
        return True

    # • Nelson Annandale, Francis Adam Marshall. Фарерские острова =
    # • The Faroes. — 1905. — 419 с.
    # ↑ Деррида Ж. Диссеминация (La Dissemination)
    if re.match(r'^\s*[•↑]', text):
        return True


def has_sent_ending(text):
    return re.search(r'[.?!…;)»"]\s*$', text)


def is_sent(text):
    return has_sent_ending(text) and not is_bib(text)


def doc_sents(sents, size=10):
    buffer = []
    for sent in sents:
        buffer.append(sent)
        if len(buffer) % size == 0:
            yield buffer
            buffer = [sent]
    if buffer:
        yield buffer


def parse_sents(sents):
    for buffer in doc_sents(sents):
        yield Partition.from_chunks(buffer)


###########
#
#   CORPORA
#
#######


def corpora_sents(records):
    for record in records:
        for par in record.pars:
            for sent in par.sents:
                if is_sent(sent.text):
                    yield sent.text


def parse_corpora_sents(records):
    sents = corpora_sents(records)
    return parse_sents(sents)


def parse_corpora_tokens(records):
    for record in records:
        for par in record.pars:
            for sent in par.sents:
                chunks = [_.text for _ in sent.tokens]
                substrings = find_substrings(chunks, sent.text)
                yield Partition.from_substrings(substrings)


#######
#
#  SYNTAG
#
#######


def syntag_sents(records):
    for record in records:
        if is_sent(record.text):
            yield record.text


def parse_syntag_sents(records):
    sents = syntag_sents(records)
    return parse_sents(sents)


def parse_syntag_tokens(records):
    for record in records:
        chunks = [_.text for _ in record.tokens if _.text]
        substrings = find_substrings(chunks, record.text)
        yield Partition.from_substrings(substrings)


######
#
#   GICRYA
#
######


def tokens_sent(tokens):
    # in case token text is _, skip it
    return ' '.join(
        _.text
        for _ in tokens
        if _.text
    )


def gicrya_sents(records):
    for record in records:
        sent = tokens_sent(record.tokens)
        if is_sent(sent):
            yield sent


def parse_gicrya_sents(records):
    sents = gicrya_sents(records)
    return parse_sents(sents)


def parse_gicrya_tokens(records):
    for record in records:
        yield Partition.from_chunks(
            _.text
            for _ in record.tokens
            if _.text
        )


#######
#
#   RNC
#
######


def rnc_sents(records):
    for record in records:
        sent = tokens_sent(record.tokens)
        if is_sent(sent):
            yield sent


def parse_rnc_sents(records):
    sents = rnc_sents(records)
    return parse_sents(sents)


def parse_rnc_tokens(records):
    for record in records:
        yield Partition.from_chunks(
            _.text
            for _ in record.tokens
            if _.text
        )
