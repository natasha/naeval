
import re

from corus import load_corpora  # noqa
from corus import load_ud_syntag as load_syntag  # noqa
from corus import load_morphoru_gicrya as load_gicrya  # noqa
from corus import load_morphoru_rnc as load_rnc  # noqa

from naeval.record import Record

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


class Buffer(Record):
    __attributes__ = ['id', 'text', 'chunks']

    def __init__(self, id=None, text=None, chunks=None):
        self.id = id
        self.text = text
        if not chunks:
            chunks = []
        self.chunks = chunks


###########
#
#   CORPORA
#
#######


def parse_corpora_sents(records):
    for record in records:
        buffer = []
        for par in record.pars:
            for sent in par.sents:
                if is_sent(sent.text):
                    buffer.append(sent.text)
        yield Partition.from_chunks(buffer)


def parse_corpora_tokens(records):
    for record in records:
        for par in record.pars:
            for sent in par.sents:
                buffer = Buffer(text=sent.text)
                for token in sent.tokens:
                    buffer.chunks.append(token.text)
                substrings = find_substrings(buffer.chunks, buffer.text)
                yield Partition.from_substrings(substrings)


#######
#
#  SYNTAG
#
#######


def syntag_doc(id):
    # sent_id = 2013Algoritm.xml_5
    match = re.match(r'^([^.]+).xml_\d+$', id)
    return match.group(1)


def parse_syntag_sents(records):
    buffer = Buffer()
    for record in records:
        id = syntag_doc(record.id)
        if buffer.chunks and buffer.id != id:
            yield Partition.from_chunks(buffer.chunks)
            buffer.chunks = []

        buffer.id = id
        if is_sent(record.text):
            buffer.chunks.append(record.text)

    if buffer.chunks:
        yield Partition.from_chunks(buffer.chunks)


def parse_syntag_tokens(records):
    for record in records:
        buffer = Buffer(text=record.text)
        for token in record.tokens:
            if token.text:
                buffer.chunks.append(token.text)
        substrings = find_substrings(buffer.chunks, buffer.text)
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


def parse_gicrya_sents(records):
    buffer = []
    for record in records:
        if buffer and len(buffer) % 191 == 0:
            yield Partition.from_chunks(buffer)
            buffer = []

        sent = tokens_sent(record.tokens)
        if is_sent(sent):
            buffer.append(sent)

    if buffer:
        yield Partition.from_chunks(buffer)


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


def parse_rnc_sents(records):
    buffer = []
    for record in records:
        if buffer and record.attrs:
            # ==> blogs.xhtml <==
            # ==newfile==
            yield Partition.from_chunks(buffer)
            buffer = []

        sent = tokens_sent(record.tokens)
        if is_sent(sent):
            buffer.append(sent)

    if buffer:
        yield Partition.from_chunks(buffer)


def parse_rnc_tokens(records):
    for record in records:
        yield Partition.from_chunks(
            _.text
            for _ in record.tokens
            if _.text
        )
