str="Hi He Lied Because B or on Could Not Oxidize Flu or ine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()
i=1
dict={}

for  s in str:
    if i==1 or i==5 or i==6 or i==7 or i==8 or i==9 or i==15 or i==16 or i==19:
        dict[s[:1]]=i
    else:
        dict[s[:2]]=i
    i+=1

print(dict)
