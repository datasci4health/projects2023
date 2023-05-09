import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

from constants import BRAZIL_MAP_GPD, PENSE_DICT

sns.set(style="whitegrid")


def break_string(string, max_len):
    if max_len is None:
        return string

    words = string.split()
    lines = []
    current_line = words[0]
    for word in words[1:]:
        if len(current_line) + 1 + len(word) <= max_len:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return '\n'.join(lines)


def plot_pie(df, cod, ax=None, max_len=None):
    question = PENSE_DICT.get_question(cod)
    df = df[cod].value_counts()

    ax = df.plot(kind='pie', autopct='%1.1f%%', labels=None, legend=True, ax=ax)
    desc_dict = PENSE_DICT.get_pv_dict(cod)
    ax.legend([desc_dict[v] for v in df.index.values])
    ax.set_ylabel('Porcentagem')
    ax.set_title(break_string(question, max_len))


def plot_geopandas(df, title=None):
    fig, ax = plt.subplots(figsize=(12, 8))
    merged = BRAZIL_MAP_GPD.merge(df, left_on='codigo_ibg', right_on='UF')
    merged.plot(column='values', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True,
                legend_kwds={'shrink': 0.8})
    ax.axis('off')
    if title is not None:
        plt.title(title)

    plt.show()


def plot_correlation(df, x, y, title='', xlabel='x', ylabel='y'):
    jg = sns.jointplot(x=x, y=y, data=df, kind='reg')

    jg.fig.suptitle(title)
    jg.fig.subplots_adjust(top=0.9)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    corr, pval = pearsonr(df[x], df[y])
    phantom, = jg.ax_joint.plot([], [], linestyle="", alpha=0)
    jg.ax_joint.legend([phantom], [f"Correlation coefficient: {corr:.2f}\nP-value: {pval:.2e}"])
    plt.show()
