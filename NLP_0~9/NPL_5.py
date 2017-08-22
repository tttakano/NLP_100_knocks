def get_word_bigram(n, str):
    word_bigram=[]
    list=str.split()
    for i in range(len(list)-(n-1)):
        word_bigram.append(list[i:i+n])
    return word_bigram

def get_charactor_bigram(n,str):
    charactor_bigram=[]
    list="".join(str.split())
    for i in range(len(list)-(n-1)):
        charactor_bigram.append(list[i:i+n])
    return charactor_bigram

str="I am an NLPer"
print(get_word_bigram(2,str))
print(get_charactor_bigram(2,str))
