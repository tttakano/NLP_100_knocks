
filename="./files/hightemp.txt"
def pick_col(filename=filename):
    col1 = open('./files/col1.txt','w')
    col2 = open('./files/col2.txt','w')
    with open(filename,"r") as f:
        for l in f:
            split=l.split()
            col1.write(split[0]+"\n")
            col2.write(split[1]+"\n")

    col1.close()
    col2.close()

if __name__ == "__main__":
    pick_col()

#confirm
#diff <(cut -f 1 ./files/hightemp.txt) <(cat ./files/col1.txt)
#diff <(cut -f 2 ./files/hightemp.txt) <(cat ./files/col2.txt)
