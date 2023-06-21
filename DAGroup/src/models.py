import copy

import numpy as np
import pandas as pd
from IPython.core.display import display
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, make_scorer, ConfusionMatrixDisplay
import seaborn as sns


def classification_metrics(model, X, y):

    y_pred = model.predict(X)

    sns.set(style="ticks")
    fig, axes = plt.subplots(1, 2, figsize=(13, 3))

    ConfusionMatrixDisplay.from_predictions(
        y,
        y_pred,
        display_labels=['S/Depre', 'Depre'],
        cmap=plt.cm.Blues,
        ax=axes[0]
    )

    ConfusionMatrixDisplay.from_predictions(
        y,
        y_pred,
        display_labels=['S/Depre', 'Depre'],
        normalize='true',
        cmap=plt.cm.Blues,
        ax=axes[1]
    )

    sns.set(style="whitegrid")

    plt.show()

    accuracy = accuracy_score(y, y_pred)
    f1 = f1_score(y, y_pred)
    precision = precision_score(y, y_pred)
    recall = recall_score(y, y_pred)

    scores = {
        "accuracy": accuracy,
        "f1_score": f1,
        "precision": precision,
        "recall": recall,
    }

    return scores


def run_model_dep_classification(model, X, y):
    # Define the scoring metrics
    scoring = {
        'acc': make_scorer(accuracy_score),
        'f1': make_scorer(f1_score),
        'precision': make_scorer(precision_score),
        'recall': make_scorer(recall_score)
    }
    # Compute cross-validated scores
    scores = cross_validate(model, X, y, cv=5, scoring=scoring, error_score='raise')

    model.fit(X, y)

    y_pred = model.predict(X)

    train_scores = {
        'acc': accuracy_score(y, y_pred),
        'f1': f1_score(y, y_pred),
        'precision': precision_score(y, y_pred),
        'recall': recall_score(y, y_pred)
    }

    data = []
    for atrib in ['acc', 'precision', 'recall', 'f1']:
        data.append(['train_{}'.format(atrib), train_scores[atrib]])
        atrib = 'test_{}'.format(atrib)
        data.append(['{}'.format(atrib), np.mean(scores[atrib])])
        data.append(['{}_std'.format(atrib), np.std(scores[atrib])])

    df_metrics = pd.DataFrame(data, columns=['metric', 'value'])
    df_metrics.set_index(df_metrics.columns[0], inplace=True)
    df_metrics = df_metrics.T
    df_metrics = df_metrics.reset_index(drop=True)
    df_metrics.columns.names = ['exp']

    return model, df_metrics


def create_df_importances(columns, slopes, bias=None):
    data = []

    if len(columns) != len(slopes):
        raise Exception("Error different len columns and slopes")

    if bias is not None:
        data.append(['intercept', bias])

    for column_name, c in zip(columns, slopes):
        data.append([column_name, c])

    df = pd.DataFrame(data, columns=['name', 'value'])
    df.set_index(df.columns[0], inplace=True)

    return df


def append_df_metrics(df, df_ap, exp):
    df = df.drop(exp, errors='ignore')
    new_df = copy.deepcopy(df_ap)
    new_df.rename(index={0: exp}, inplace=True)
    df = pd.concat((df, new_df))
    return df


def append_df_importances(df, df_ap, exp):
    df = df.T
    df_ap = df_ap.T

    df = df.drop(exp, errors='ignore')
    new_df = copy.deepcopy(df_ap)
    new_df.rename(index={'value': exp}, inplace=True)
    df = pd.concat((df, new_df))
    return df.T
