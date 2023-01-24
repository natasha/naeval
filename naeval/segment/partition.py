
import re

from naeval.record import Record

from .substring import Substring


FILL = ' '
FILL_PATTERN = re.compile(r'^\s*$')


class Partition(Record):
    __attributes__ = ['chunks']

    is_fill = FILL_PATTERN.match

    def __init__(self, chunks):
        self.chunks = chunks

    @property
    def text(self):
        return ''.join(self.chunks)

    @property
    def substrings(self):
        start = 0
        for chunk in self.chunks:
            stop = start + len(chunk)
            if not self.is_fill(chunk):
                yield Substring(start, stop, chunk)
            start = stop

    @property
    def splits(self):
        previous = None
        for substring in self.substrings:
            if previous:
                yield previous, substring.start
            previous = substring.stop

    @classmethod
    def from_chunks(cls, chunks):
        chunks = list(fill_chunks(chunks))
        return cls(chunks)

    @classmethod
    def from_substrings(cls, substrings):
        chunks = list(substring_chunks(substrings))
        return cls(chunks)


def substring_chunks(substrings, fill=FILL):
    previous = 0
    for index, substring in enumerate(substrings):
        if index > 0:
            size = substring.start - previous
            if size:
                yield fill * size
        yield substring.text
        previous = substring.stop


def fill_chunks(chunks, fill=FILL):
    for index, chunk in enumerate(chunks):
        if index > 0:
            yield fill
        yield chunk


########
#
#   IO
#
#####


SEP = '|'
ESCAPE = [
    (SEP, '/'),
    ('\n', ' ')
]


def escape_chunk(chunk):
    for source, target in ESCAPE:
        chunk = chunk.replace(source, target)
    return chunk


def format_partition(partition):
    return SEP.join(escape_chunk(_) for _ in partition.chunks)


def show_partition(partition):
    print(format_partition(partition))


def format_partitions(partitions):
    for partition in partitions:
        yield format_partition(partition)


def parse_partition(line):
    chunks = line.split(SEP)
    return Partition(chunks)


def parse_partitions(lines):
    for line in lines:
        yield parse_partition(line)
