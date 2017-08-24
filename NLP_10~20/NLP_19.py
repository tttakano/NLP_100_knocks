
filename="./files/hightemp.txt"

def frequency(filename=filename):
    dict={}
    with open(filename,"r") as f:
        for col in f:
            col=col.split()
            if dict.has_key(col[0]):
                dict[col[0]]+=1
            else:
                dict[col[0]]=1
    dict=sorted(dict.items(), key=lambda x: x[1],reverse=True)
    return dict

if __name__=="__main__":
    dict=frequency()
    for d in dict:
        print(d[1]),
        print(d[0])

#cut -f 1 ./files/hightemp.txt | sort | uniq -c | sort -r
