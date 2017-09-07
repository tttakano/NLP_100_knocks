import CaboCha
from prettyprint import pp

filename="./files/neko.txt"
output="./files/neko.txt.cabocha"

def cabocha_neko():
    with open(filename) as infile, open(output,"w") as outfile:
        cabocha=CaboCha.Parser()
        for line in infile:
            outfile.write(cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE))

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface=surface
        self.base=base
        self.pos=pos
        self.pos1=pos1

    def __str__(self):
        return "surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]"\
            .format(self.surface,self.base,self.pos,self.pos1)

def read_cabocha():
    with open(output) as outfile:
        morphs=[]
        for line in outfile:
            if line=="EOS\n":
                yield morphs
                morphs=[]

            else:
                if line[0]=="*":
                    continue

                cols=line.split("\t")
                res_cols=cols[1].split(",")

                morphs.append(Morph(
                    cols[0],res_cols[6],res_cols[0],res_cols[1]
                ))

if __name__=="__main__":
    #chabocha_neko()
    for i,morphs in enumerate(read_cabocha(),1):
        if i==3:
            for morph in morphs:
                print(morph)
            break
