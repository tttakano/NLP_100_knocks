# coding: utf-8
import MeCab
from prettyprint import pp
output = "./files/neko.txt.mecab"


def make_list():
    with open(output) as f:
        sentences = []
        for line in f:
            splited = line.split("\t")
            if(len(splited) < 2):
                break
            factor = splited[1].split(",")
            sentence = {
                'surface': splited[0],
                'base': factor[6],
                'pos': factor[0],
                'pos1': factor[1]
            }
            sentences.append(sentence)

            if factor[1] == "句点":
                yield sentences
                sentences = []


if __name__ == "__main__":
    np = set()
    np_test = []
    for cols in make_list():
        for i in range(1, len(cols) - 1):
            if cols[i]["surface"] == "の" \
                    and cols[i - 1]["pos"] == "名詞" \
                    and cols[i + 1]["pos"] == "名詞":
                np_test.append(cols[i - 1]["surface"] + cols[i]
                               ["surface"] + cols[i + 1]["surface"])
                np.add(cols[i - 1]["surface"] + cols[i]
                       ["surface"] + cols[i + 1]["surface"])

    pp(sorted(np, key=np_test.index))
