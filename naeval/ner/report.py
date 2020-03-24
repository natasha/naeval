
import pandas as pd

from naeval.report import table_html
from naeval.report import Bench, format_bench_report  # noqa
from naeval.const import (
    PER, LOC, ORG,
    GAREEV,
)


def scores_report_table(scores, datasets, models, types=[PER, LOC, ORG]):
    data = []
    for dataset in datasets:
        for model in models:
            for type in types:
                score = scores[dataset, model][type]
                data.append([dataset, model, type, score])
    table = pd.DataFrame(data, columns=['dataset', 'model', 'type', 'score'])
    table = table.set_index(['dataset', 'model', 'type']).unstack(['dataset', 'type'])

    table.columns = table.columns.droplevel()
    table.index.name = None

    columns = [
        (dataset, type)
        for dataset in datasets
        for type in types
    ]
    table = table.reindex(index=models, columns=columns)

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

    return table_html(output)


def format_github_scores_column(column, top=3):
    column = [
        (_.value if _ else None)
        for _ in column
    ]

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

    return table_html(output)
