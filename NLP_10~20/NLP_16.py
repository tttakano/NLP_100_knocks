import sys
import shutil
import math
from NLP_10 import col_count
filename="./files/hightemp.txt"
args=sys.argv

def split(filename=filename):
    count=col_count()
    number=math.ceil(count/float(args[1]))
    f = open(filename,'r')
    data=f.readlines()
    f.close()

    for fn in range(int(args[1])):
        with open("./files/written"+str(fn)+".txt","w") as w:
                for cl in range(int(number)):
                    if fn*int(number)+cl < count:
                        write=data[fn*int(number)+cl]
                        w.write(write)

if __name__=="__main__":
    split()


#split -l 5 ./files/hightemp.txt out.
