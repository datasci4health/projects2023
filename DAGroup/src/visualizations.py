import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

from constants import BRAZIL_MAP_GPD

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


def plot_pie(df, cod, title, desc_dict=None, ax=None, max_len=None):
    df = df[cod].value_counts()
    ax = df.plot(kind='pie', autopct='%1.1f%%', labels=None, legend=True, ax=ax)
    if desc_dict is not None:
        ax.legend([desc_dict[v] for v in df.index.values], fontsize='small')
    ax.set_ylabel('Porcentagem')
    ax.set_title(break_string(title, max_len))


def plot_bar(df, cod, title, desc_dict=None, ax=None, max_len=None):
    df = df[cod].value_counts(normalize=True) * 100
    df = df.sort_index()
    if desc_dict is not None:
        df = df.rename(index=desc_dict)
    ax = df.plot(kind='bar', ax=ax, width=0.8, legend=False)
    ax.set_ylabel('Porcentagem')
    # Set the x-axis tick labels at a diagonal angle
    ax.set_xticklabels(df.index, rotation=45, ha='right')
    ax.set_xlabel('')
    ax.set_title(break_string(title, max_len))


def plot_dist(data, title, ax=None, max_len=None):
    sns.histplot(data, bins=20, kde=True, ax=ax, stat='percent')
    ax.set_ylabel('Porcentagem')
    ax.set_xlabel('')
    ax.set_title(break_string(title, max_len))


def plot_geopandas(df, uf_key, title=None):
    fig, ax = plt.subplots(figsize=(12, 8))
    merged = BRAZIL_MAP_GPD.merge(df, left_on='codigo_ibg', right_on=uf_key)
    merged.plot(column='values', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True,
                legend_kwds={'shrink': 0.8})
    ax.axis('off')
    if title is not None:
        plt.title(title)

    plt.show()

    return fig


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

    return jg.fig
