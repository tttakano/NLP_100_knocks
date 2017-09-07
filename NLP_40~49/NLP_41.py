import CaboCha
import re
from prettyprint import pp

filename = "./files/neko.txt"
output = "./files/neko.txt.cabocha"


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]"\
            .format(self.surface, self.base, self.pos, self.pos1)


class Chunk:
    def __init__(self):
        self.morphs = []
        self.srcs = []
        self.dst = -1

    def __str__(self):
        surface = ""
        for morph in self.morphs:
            surface += morph.surface
        return "{}\tsrcs{}\tdst[{}]".format(surface, self.srcs, self.dst)


def read_cabocha():
    with open(output) as outfile:
        chunks = dict()
        idx = -1

        for line in outfile:
            if line == "EOS\n":
                if len(chunks) > 0:
                    sorted_tuple = sorted(chunks.items(), key=lambda x: x[0])
                    yield list(zip(*sorted_tuple))[1]
                    chunks.clear()

                else:
                    yield []

            elif line[0] == "*":
                cols = line.split(" ")
                idx = int(cols[1])
                dst = int(re.search(r"(.*?)D", cols[2]).group(1))
                if idx not in chunks:
                    chunks[idx] = Chunk()
                chunks[idx].dst = dst
                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    chunks[dst].srcs.append(idx)

            else:
                cols = line.split("\t")
                res_cols = cols[1].split(",")
                chunks[idx].morphs.append(
                    Morph(
                        cols[0],
                        res_cols[6],
                        res_cols[0],
                        res_cols[1]
                    )
                )


if __name__ == "__main__":
    for i, chunk in enumerate(read_cabocha(), 1):

        if i == 8:
            for j, chunk in enumerate(chunk):
                print("[{}]{}".format(j, chunk))
            break
