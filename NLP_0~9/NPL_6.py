def get_charactor_bigram(n,str):
    charactor_bigram=set({})
    for i in range(len(str)-(n-1)):
        charactor_bigram.add(str[i:i+n])
    return charactor_bigram

str1="paraparaparadise"
str2="paragraph"

X=get_charactor_bigram(2,str1)
Y=get_charactor_bigram(2,str2)
print(X)
print(Y)
print(X&Y)
print(X|Y)
print(X-Y)
print(Y-X)
print('se' in X)
print('se' in Y)
