
import pandas as pd

from naeval.report import table_html


def report_table(scores, times, sources, segmenters, type):
    data = []
    segmenters = segmenters[type]
    for seg in segmenters:
        label = segmenters[seg].label
        for source in sources:
            errors = scores[type, seg, source]
            time = times[type, seg, source]
            data.append([label, source, errors.prec, errors.recall, time])
    return pd.DataFrame(
        data,
        columns=['seg', 'source', 'prec', 'recall', 'time']
    )


def format_column(column, name, github, top=3):
    best = (
        column[1:]   # skip baseline
        if len(column) > 1
        else column
    ).nsmallest(top)
    for value in column:
        string = (
            '{:.1f}'
            if name == 'time'
            else '{:.0f}'
        ).format(value)
        if github and value in best.values:
            string = '<b>%s</b>' % string
        yield string


def format_report(table, github=False):
    segs = table.seg.unique()
    sources = table.source.unique()

    table['errors'] = table.prec + table.recall
    metrics = ['errors', 'prec', 'recall', 'time']
    table = table.pivot('seg', 'source', metrics)
    table = table.swaplevel(axis=1)
    if github:
        metrics = ['errors', 'time']

    table = table.reindex(
        index=segs,
        columns=[
            (source, metric)
            for source in sources
            for metric in metrics
        ]
    )

    for source in sources:
        for metric in metrics:
            column = table[source, metric]
            table[source, metric] = list(format_column(column, metric, github))

    table.index.name = None
    table.columns.names = None, None
    return table_html(table)
