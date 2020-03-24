
import pandas as pd

from naeval.report import table_html
from naeval.report import Bench, format_bench_report  # noqa


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


def format_scores_column(column, top=2):
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
