# -*- coding: utf-8 -*-
import json
import gzip
import re
from NLP_20 import get_data
from NLP_21 import get_category_line


def get_category_name():
    pattern = re.compile(r"(.*Category:)(\w*[ぁ-んァ-ン]*[一-龥]*)(\|?.*)")
    for line in get_category_line():
        print(pattern.search(line).group(2))


if __name__ == "__main__":
    get_category_name()
