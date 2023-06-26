import copy

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import cross_validate
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, make_scorer, \
    ConfusionMatrixDisplay, roc_curve, roc_auc_score
import seaborn as sns
from sklearn.tree._tree import TREE_LEAF
from sklearn.base import BaseEstimator, TransformerMixin


def plot_cm(model, X, y, path=None):
    y_pred = model.predict(X)
    sns.set(style="ticks")
    fig, axes = plt.subplots(1, 2, figsize=(11, 3))

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
    # sns.set(style="whitegrid")

    if path is not None:
        fig.savefig(path)

    plt.show()


def plot_roc_curve(model_dict, X, y, path=None):
    fig = plt.figure()

    for key, model in model_dict.items():
        # Make predictions on the test set
        y_pred_prob = model.predict_proba(X)[:, 1]  # Probability of the positive class
        # Calculate the false positive rate, true positive rate, and thresholds
        fpr, tpr, thresholds = roc_curve(y, y_pred_prob)
        # Calculate the area under the ROC curve
        auc = roc_auc_score(y, y_pred_prob)
        # Plot the ROC curve
        plt.plot(fpr, tpr, label=key + ': AUC = %0.3f' % auc)
        plt.plot([0, 1], [0, 1], 'k--')  # Diagonal line representing random guessing

    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc='lower right')

    if path is not None:
        fig.savefig(path)

    plt.show()


def classification_metrics(model_dict, X_train, y_train, X_test, y_test):
    data = []

    for key, model in model_dict.items():
        y_pred = model.predict(X_train)
        y_pred_prob = model.predict_proba(X_train)[:, 1]

        accuracy = accuracy_score(y_train, y_pred)
        f1 = f1_score(y_train, y_pred)
        precision = precision_score(y_train, y_pred)
        recall = recall_score(y_train, y_pred)
        auc = roc_auc_score(y_train, y_pred_prob)

        y_pred = model.predict(X_test)
        y_pred_prob = model.predict_proba(X_test)[:, 1]

        accuracy_t = accuracy_score(y_test, y_pred)
        f1_t = f1_score(y_test, y_pred)
        precision_t = precision_score(y_test, y_pred)
        recall_t = recall_score(y_test, y_pred)
        auc_t = roc_auc_score(y_test, y_pred_prob)

        data.append([key, accuracy, precision, recall, f1, auc, accuracy_t, precision_t, recall_t, f1_t, auc_t])

    return pd.DataFrame(data,
                        columns=['exp', 'accuracy_train', 'precision_train', 'recall_train', 'f1_train', 'auc_train',
                                 'accuracy_test', 'precision_test', 'recall_test', 'f1_test', 'auc_test'])


def run_model_dep_classification(model, X, y):
    # Define the scoring metrics
    scoring = {
        'acc': make_scorer(accuracy_score),
        'f1': make_scorer(f1_score),
        'precision': make_scorer(precision_score),
        'recall': make_scorer(recall_score),
        'auc': make_scorer(roc_auc_score)
    }
    # Compute cross-validated scores
    scores = cross_validate(model, X, y, cv=5, scoring=scoring, error_score='raise')

    model.fit(X, y)

    y_pred = model.predict(X)
    y_pred_prob = model.predict(X)

    train_scores = {
        'acc': accuracy_score(y, y_pred),
        'f1': f1_score(y, y_pred),
        'precision': precision_score(y, y_pred),
        'recall': recall_score(y, y_pred),
        'auc': roc_auc_score(y, y_pred_prob)
    }

    data = []
    for atrib in ['acc', 'precision', 'recall', 'f1', 'auc']:
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


def is_leaf(inner_tree, index):
    # Check whether node is leaf node
    return (inner_tree.children_left[index] == TREE_LEAF and
            inner_tree.children_right[index] == TREE_LEAF)


def prune_index(inner_tree, decisions, index=0):
    # Start pruning from the bottom - if we start from the top, we might miss
    # nodes that become leaves during pruning.
    # Do not use this directly - use prune_duplicate_leaves instead.
    if not is_leaf(inner_tree, inner_tree.children_left[index]):
        prune_index(inner_tree, decisions, inner_tree.children_left[index])
    if not is_leaf(inner_tree, inner_tree.children_right[index]):
        prune_index(inner_tree, decisions, inner_tree.children_right[index])

    # Prune children if both children are leaves now and make the same decision:
    if (is_leaf(inner_tree, inner_tree.children_left[index]) and
            is_leaf(inner_tree, inner_tree.children_right[index]) and
            (decisions[index] == decisions[inner_tree.children_left[index]]) and
            (decisions[index] == decisions[inner_tree.children_right[index]])):
        # turn node into a leaf by "unlinking" its children
        inner_tree.children_left[index] = TREE_LEAF
        inner_tree.children_right[index] = TREE_LEAF
        ##print("Pruned {}".format(index))


def prune_duplicate_leaves(mdl):
    # Remove leaves if both
    decisions = mdl.tree_.value.argmax(axis=2).flatten().tolist()  # Decision for each node
    prune_index(mdl.tree_, decisions)


class RoundTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = np.round(X)
        return X
