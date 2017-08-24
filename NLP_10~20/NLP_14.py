import sys

filename="./files/hightemp.txt"
args=sys.argv
def head(filename=filename):
    with open(filename,"r") as f:
        for i,col in enumerate(f):
            col=col.rstrip("\r\n")
            if i >= int(args[1]):
                break
            print(col)

if __name__=="__main__":
    head()


#diff <(head -n 2 ./files/hightemp.txt) <(python NLP_14.py 2)
