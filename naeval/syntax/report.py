
import pandas as pd

from naeval.report import table_html
from naeval.report import Bench, bench_report_table, format_bench_report  # noqa
from naeval.report import format_sec, format_mb, format_speed


def scores_report_table(scores, datasets, models):
    data = []
    for dataset in datasets:
        for model in models:
            score = scores[dataset, model]
            data.append([dataset, model, score.uas.value, score.las.value])
    table = pd.DataFrame(data, columns=['dataset', 'model', 'uas', 'las'])

    table = table.set_index(['model', 'dataset']).stack().reset_index()
    table.columns = ['model', 'dataset', 'type', 'value']

    table = table.set_index(['dataset', 'model', 'type']).unstack(['dataset', 'type'])
    table.columns = table.columns.droplevel()
    table.index.name = None

    columns = [
        (dataset, type)
        for dataset in datasets
        for type in ['uas', 'las']
    ]
    table = table.reindex(index=models, columns=columns)

    return table


def format_scores_column(column, top=3):
    selection = sorted(column)[-top:]

    for value in column:
        cell = '%.3f' % value
        if value in selection:
            cell = '<b>%s</b>' % cell
        yield cell


def format_scores_report(table):
    output = pd.DataFrame()
    for column in table.columns:
        output[column] = list(format_scores_column(table[column]))
    output.index = table.index
    output.columns = pd.MultiIndex.from_tuples(output.columns)
    return table_html(output)


def format_natasha_report(scores, bench, dataset, models):
    scores = scores.loc[models][dataset]
    bench = bench.loc[models]

    output = pd.DataFrame()
    for type in ['uas', 'las']:
        output[type] = [
            '%.3f' % _
            for _ in scores[type]
        ]

    columns = [
        ['init', format_sec, 'init, s'],
        ['disk', format_mb, 'disk, mb'],
        ['ram', format_mb, 'ram, mb'],
        [['speed', 'device'], format_speed, 'speed, sents/s']
    ]
    for slice, format, name in columns:
        values = bench[slice].values.tolist()
        output[name] = [format(_) for _ in values]

    output.index = models
    return table_html(output)
