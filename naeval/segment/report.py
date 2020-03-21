
import pandas as pd

from naeval.report import table_html


def report_table(scores, times, datasets, models, type):
    data = []
    models = models[type]
    for model in models:
        label = models[model].label
        for dataset in datasets:
            time = times[type, model, dataset]
            score = scores[type, model, dataset]
            prec = score.prec.total - score.prec.correct
            recall = score.recall.total - score.recall.correct
            data.append([label, dataset, prec, recall, time])
    return pd.DataFrame(
        data,
        columns=['model', 'dataset', 'prec', 'recall', 'time']
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
    models = table.model.unique()
    datasets = table.dataset.unique()
    metrics = ['errors', 'prec', 'recall', 'time']

    table['errors'] = table.prec + table.recall
    table = table.pivot('model', 'dataset', metrics)
    table = table.swaplevel(axis=1)
    if github:
        metrics = ['errors', 'time']

    table = table.reindex(
        index=models,
        columns=[
            (dataset, metric)
            for dataset in datasets
            for metric in metrics
        ]
    )

    for dataset in datasets:
        for metric in metrics:
            column = table[dataset, metric]
            table[dataset, metric] = list(format_column(column, metric, github))

    table.index.name = None
    table.columns.names = None, None
    return table_html(table)
