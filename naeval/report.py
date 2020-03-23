
import pandas as pd

from .record import Record
from .const import CPU, GPU, MB


def table_html(table):
    html = table.to_html(escape=False)  # <b>...</b> highlights
    html = html.replace('border="1"', 'border="0"')  # for github
    return html


#########
#
#   BENCH
#
##########


class Bench(Record):
    __attributes__ = ['model', 'init', 'disk', 'ram', 'speed', 'device']

    def __init__(self, model, init=None, disk=None, ram=None,
                 speed=None, device=CPU):
        self.model = model
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


def format_bench_report(records, models):
    table = pd.DataFrame()

    mapping = {_.model: _ for _ in records}
    records = [mapping[_] for _ in models]

    columns = [
        [slice_init, format_sec, select_min, 'init, s'],
        [slice_disk, format_mb, select_min, 'disk, mb'],
        [slice_ram, format_mb, select_min, 'ram, mb'],
        [slice_speed, format_speed, select_max, 'speed, it/s']
    ]
    for slice, format, select, name in columns:
        values = list(slice(records))
        selection = select(values)
        table[name] = list(highlight(values, selection, format))

    table.index = models
    table.index.name = None
    return table_html(table)
