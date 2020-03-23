
import pandas as pd

from naeval.report import table_html
from naeval.report import Bench, format_bench_report  # noqa


def scores_report_table(scores, datasets, models):
    data = []
    for dataset in datasets:
        for model in models:
            score = scores[dataset, model]
            data.append([dataset, model, score.value])
    table = pd.DataFrame(data, columns=['dataset', 'model', 'acc'])
    table = table.pivot(index='model', columns='dataset', values='acc')
    table = table.reindex(index=models, columns=datasets)
    table.index.name = None
    table.columns.name = None
    return table


def format_scores_column(column, top=3):
    selection = None
    selection = sorted(column)[-top:]

    for value in column:
        cell = ''
        if value:
            cell = '%.3f' % value
        if value in selection:
            cell = '<b>%s</b>' % cell
        yield cell


def format_scores_report(table):
    output = pd.DataFrame()
    for column in table.columns:
        output[column] = list(format_scores_column(table[column]))
    output.index = table.index
    return table_html(output)
