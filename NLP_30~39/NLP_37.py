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
    word_list = counter.most_common(10)
    return word_list


if __name__ == "__main__":
    size = 10
    count = get_counter()
    list_count = list(zip(*count))
    words = list_count[0]
    counts = list_count[1]

    plt.bar(
        range(0, size),
        counts,
        align='center'
    )

    plt.xticks(
        range(0, size),
        [unicode(word, "utf-8") for word in words],
    )

    plt.xlim(
        xmin=-1, xmax=size
    )

    plt.title(
        'most frequency 10 words',
    )

    plt.xlabel(
        'top 10 words',
    )
    
    plt.ylabel(
        'frequency',
    )

    plt.grid(axis='y')

    plt.show()
