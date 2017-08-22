# -*- coding: utf-8 -*-
import re

def chiper(str):
    ans=""
    for s in str:
        if re.match(r"[a-z]",s):
            s=chr(219-ord(s))
        ans+=s
    return ans
    
str="i have 9 pens a z"
chip=chiper(str)
print("暗号化 "+chip)
print("復号化 "+chiper(chip))
