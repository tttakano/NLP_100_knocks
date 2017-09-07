# -*- coding: utf-8 -*-
import json
import gzip
import re
from NLP_20 import get_data
from NLP_25 import get_fund_infomation


def remove_markup(fund):
    pattern = re.compile(r"\'{2,5}", re.MULTILINE)
    for key, value in fund.items():
        fund[key] = pattern.sub("", value)

    return fund


if __name__ == "__main__":
    fund = remove_markup(get_fund_infomation())
    for key, value in fund.items():
        print(value)
