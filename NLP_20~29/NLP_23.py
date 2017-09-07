# -*- coding: utf-8 -*-
import re
from NLP_20 import get_data


def get_section_level():
    data = get_data()
    pattern = re.compile(r"^(={2,})\s*(.+?)\s*\1.*$", re.MULTILINE)
    return pattern.findall(data)


if __name__ == "__main__":
    for data in get_section_level():
        level = len(data[0]) - 1
        print(str(level) + " " + data[1])
