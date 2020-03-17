
import pandas as pd

from naeval.record import Record
from naeval.const import (
    PER, LOC, ORG,
    GAREEV,
    CPU, GPU, MB
)


def scores_report_table(scores, sources, annotators, types=[PER, LOC, ORG]):
    data = []
    for source in sources:
        for annotator in annotators:
            for type in types:
                score = scores[source, annotator][type]
                data.append([source, annotator, type, score])
    table = pd.DataFrame(data, columns=['source', 'annotator', 'type', 'score'])
    table = table.set_index(['source', 'annotator', 'type']).unstack(['source', 'type'])

    table.columns = table.columns.droplevel()
    table.index.name = None

    columns = [
        (source, type)
        for source in sources
        for type in types
    ]
    table = table.reindex(index=annotators, columns=columns)

    return table


def format_score(value):
    if not value:
        return '-'
    return '{0:02d}'.format(int(value * 100))


def format_scores(scores):
    return '{prec}/{recall}/{f1}'.format(
        prec=format_score(scores.prec.value),
        recall=format_score(scores.recall.value),
        f1=format_score(scores.value)
    )


def format_scores_report(table):
    output = pd.DataFrame()
    for column in table.columns:
        output[column] = table[column].map(format_scores)

    output.columns = pd.MultiIndex.from_tuples(output.columns)
    output.columns.names = [None, 'prec/recall/f1,%']

    return output


def format_github_scores_column(column, top=3):
    column = [
        (_.value if _ else None)
        for _ in column
    ]

    selection = None
    values = list(filter(None, column))
    selection = sorted(values)[-top:]

    for value in column:
        cell = ''
        if value:
            cell = '%.3f' % value
        if value in selection:
            cell = '<b>%s</b>' % cell
        yield cell


def format_github_scores_report(table):
    output = pd.DataFrame()
    for column in table.columns:
        dataset, type = column
        if dataset == GAREEV and type == LOC:
            continue
        output[column] = list(format_github_scores_column(table[column]))

    output.index = table.index
    output.columns = pd.MultiIndex.from_tuples(output.columns)
    output.columns.names = [None, 'f1']

    return output


#########
#
#   BENCH
#
##########


class Bench(Record):
    __attributes__ = ['annotator', 'init', 'disk', 'ram', 'speed', 'device']

    def __init__(self, annotator, init=None, disk=None, ram=None,
                 speed=None, device=CPU):
        self.annotator = annotator
        self.init = init
        self.disk = disk
        self.ram = ram
        self.speed = speed
        self.device = device


def select_max(values, count=3):
    return sorted(values)[-count:]


def select_min(values, count=3):
    return sorted(values)[:count]


def slice_attr(records, attr):
    for record in records:
        yield getattr(record, attr)


def slice_init(records):
    return slice_attr(records, 'init')


def slice_disk(records):
    return slice_attr(records, 'disk')


def slice_ram(records):
    return slice_attr(records, 'ram')


def slice_speed(records):
    for record in records:
        yield record.speed, record.device == GPU


def highlight(column, selection, format):
    for value in column:
        select = value in selection
        value = format(value)
        if select:
            value = '<b>%s</b>' % value
        yield value


def format_mb(bytes):
    mb = bytes / MB
    return '%0.0f' % mb


def format_sec(secs):
    return '%0.1f' % secs


def format_speed(value):
    its, gpu = value
    value = '%0.1f' % its
    if gpu:
        value += ' (gpu)'
    return value


def format_bench_report(records, annotators):
    table = pd.DataFrame()

    mapping = {_.annotator: _ for _ in records}
    records = [mapping[_] for _ in annotators]

    columns = [
        [slice_init, format_sec, select_min, 'init, s'],
        [slice_disk, format_mb, select_min, 'disk, mb'],
        [slice_ram, format_mb, select_min, 'ram, mb'],
        [slice_speed, format_speed, select_max, 'speed, articles/s']
    ]
    for slice, format, select, name in columns:
        values = list(slice(records))
        selection = select(values)
        table[name] = list(highlight(values, selection, format))

    table.index = annotators
    table.index.name = None
    return table
