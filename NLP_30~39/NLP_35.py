# coding: utf-8
import MeCab
from NLP_30 import make_list
from prettyprint import pp

def get_np():
    connects = []
    for cols in make_list():
        connect = []
        for col in cols:
            if col["pos"] == "名詞":
                connect.append(col["surface"])
            else:
                if len(connect) > 1:
                    connects.append("".join(connect))
                connect = []
        if len(connect) > 1:
            connects.append("".join(connect))

    np = set(connects)

    pp(sorted(np, key=connects.index))


if __name__ == "__main__":
    get_np()
