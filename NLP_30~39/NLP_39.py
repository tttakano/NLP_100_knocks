# coding: utf-8
import MeCab
from NLP_30 import make_list
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties
from collections import Counter
from prettyprint import pp


def get_counter():
    counter = Counter()
    for cols in make_list():
        counter.update([col["surface"] for col in cols])
    word_list = counter.most_common()
    return word_list


if __name__ == "__main__":
    size = 10
    count = get_counter()
    list_count = list(zip(*count))
    words = list_count[0]
    counts = list_count[1]

    plt.scatter(
        range(1,len(counts)+1),
        counts
    )

    plt.xlim(1,len(counts)+1)
    plt.ylim(1,counts[0])

    plt.xscale("log")
    plt.yscale("log")

    plt.title(
        'Rule of Zipf',
    )

    plt.xlabel(
        'number of frequency',
    )

    plt.ylabel(
        'frequency',
    )

    plt.grid(axis='both')

    plt.show()
