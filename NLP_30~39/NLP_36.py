# coding: utf-8
import MeCab
from NLP_30 import make_list
from collections import Counter
from prettyprint import pp


def get_counter():
    counter = Counter()
    for cols in make_list():
        counter.update([col["surface"] for col in cols])
    word_list = counter.most_common()
    return word_list


if __name__ == "__main__":
    pp(get_counter())
