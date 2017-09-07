import json
import gzip
import re
from NLP_20 import get_data
filename="./files/jawiki-country.json.gz"



def get_category_line():
    return re.findall(r".*Category.*$",get_data(),re.MULTILINE)

if __name__=="__main__":
    for line in get_category_line():
        print(line)
