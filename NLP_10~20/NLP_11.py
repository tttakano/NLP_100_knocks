
filename="./files/hightemp.txt"
def replace_tab(filename=filename):
    with open(filename,"r") as f:
        for col in f:
            print(" ".join(col.split()))

if __name__ == "__main__":
    replace_tab()


#confirm
#diff <(expand -t 1 ./files/hightemp.txt) <(python NLP_11.py)
