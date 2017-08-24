
filename="./files/hightemp.txt"
def col_count(filename=filename):
    with open(filename,"r") as f:
        for count,damy in enumerate(f):
            pass
    return count+1

if __name__ == "__main__":
    print(col_count())
