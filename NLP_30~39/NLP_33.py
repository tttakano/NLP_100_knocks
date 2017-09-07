# coding: utf-8
import MeCab
from prettyprint import pp
filename = "./files/neko.txt"
output = "./files/neko.txt.mecab"


def append_mecab():
    with open(filename) as data, open(output, "w") as out:
        mc = MeCab.Tagger()
        out.write(mc.parse(data.read()))


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
    verbs_test = [col["surface"]
                  for cols in make_list()
                  for col in cols
                  if col["pos"] == "名詞" and col["pos1"] == "サ変接続"]
    verbs = set(verbs_test)

    pp(sorted(verbs, key=verbs_test.index))
