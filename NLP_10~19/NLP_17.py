
filename="./files/hightemp.txt"

def collect_set(filename=filename):
    _set=set()
    with open(filename,"r") as f:
        for col in f:
            first=col.split()[0]
            _set.add(first)
    return _set



if __name__=="__main__":
    _set=collect_set()
    for i in _set:
        print(i)

#cut -f 1 hightemp.txt | sort | uniq
