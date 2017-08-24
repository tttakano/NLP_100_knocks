import sys
from NLP_10 import col_count

filename="./files/hightemp.txt"
args=sys.argv
def tail():
    count=col_count()
    with open(filename, "r") as f:
        for i,col in enumerate(f):
            col=col.rstrip("\r\n")
            if i >= count-int(args[1]):
                print(col)

if __name__=="__main__":
    tail()

#diff <(tail -n 2 ./files/hightemp.txt) <(python NLP_15.py 2)
