import random
str="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .".split()
ans=[]
for word in str:
    if len(word)>4:
        store=""
        chr=[]
        for s in word:
             chr.append(s)
        rand=chr[1:-1]
        random.shuffle(rand)
        store+=chr[0]+"".join(rand)+chr[-1]
    else:
        store=word
    ans.append(store)
print(ans)
