# -*- coding: utf-8 -*-
import json
import gzip
import re
from NLP_20 import get_data

def get_file():
    data=get_data()
    pattern=re.compile(r"(?:File|ファイル):(.+?)\|",re.MULTILINE)
    return pattern.findall(data)

if __name__=="__main__":
    for files in get_file():
        print(files)
