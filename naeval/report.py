
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
    its, device = value
    value = '%0.1f' % its
    if device == GPU:
        value += ' (gpu)'
    return value


def bench_report_table(records, models):
    table = pd.DataFrame(
        records,
        columns=['model', 'init', 'disk', 'ram', 'speed', 'device']
    )
    table = table.set_index('model')
    table.index.name = None
    return table.reindex(index=models)


def format_bench_report(table):
    output = pd.DataFrame()
    columns = [
        ['init', format_sec, select_min, 'init, s'],
        ['disk', format_mb, select_min, 'disk, mb'],
        ['ram', format_mb, select_min, 'ram, mb'],
        [['speed', 'device'], format_speed, select_max, 'speed, it/s']
    ]
    for slice, format, select, name in columns:
        values = table[slice].values.tolist()
        selection = select(values)
        output[name] = list(highlight(values, selection, format))

    output.index = table.index
    return table_html(output)
