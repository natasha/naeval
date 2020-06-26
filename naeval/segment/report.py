
import pandas as pd

from naeval.report import table_html


def model_labels(models, type):
    models = models[type]
    for name in models:
        yield name, models[name].label


def report_table(scores, times, datasets, models, type):
    data = []
    models = models[type]
    for model in models:
        for dataset in datasets:
            time = times[type, model, dataset]
            score = scores[type, model, dataset]
            prec = score.prec.total - score.prec.correct
            recall = score.recall.total - score.recall.correct
            total = score.recall.total + 1  # num of splits + 1 in etalon
            data.append([model, dataset, prec, recall, time, total])
    return pd.DataFrame(
        data,
        columns=['model', 'dataset', 'prec', 'recall', 'time', 'total']
    )


def format_column(column, name, top=3):
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
        if value in best.values:
            string = '<b>%s</b>' % string
        yield string


def format_report(table, labels, scale=1000):
    models = table.model.unique()
    datasets = table.dataset.unique()
    metrics = ['errors', 'time']

    table['errors'] = (table.prec + table.recall) / table.total * scale
    table = table.pivot('model', 'dataset', metrics)
    table = table.swaplevel(axis=1)
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
            table[dataset, metric] = list(format_column(column, metric))

    table.index.name = None
    table.columns.names = None, None
    table.index = [labels.get(_, _) for _ in table.index]
    return table_html(table)
