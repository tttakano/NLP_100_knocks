
filename="./files/hightemp.txt"
def marge_file(filename=filename):
    col1 = open('./files/col1.txt','r')
    col2 = open('./files/col2.txt','r')
    marge = open('./files/marge.txt','w')

    for a,b in zip(col1,col2):
        a=a.rstrip("\r\n")
        b=b.rstrip("\r\n")
        marge.write(a+"\t"+b+"\n")
    col1.close()
    col2.close()
    marge.close()

if __name__=="__main__":
    marge_file()

#diff <(paste ./files/col1.txt ./files/col2.txt) <(cat ./files/marge.txt)
