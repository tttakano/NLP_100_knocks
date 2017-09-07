
filename="./files/hightemp.txt"

def revered_sort(filename=filename):
    list=[]
    with open(filename,"r") as f:
        for col in f:
            col=col.split()
            list.append(col)

    list.sort(key=lambda x: x[2],reverse=True)
    return list

if __name__=="__main__":
    list=revered_sort()
    for l in list:
        print(l[2])

#sort -nk3 -r ./files/hightemp.txt 
