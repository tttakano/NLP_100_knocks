# -*- coding: utf-8 -*-
import re
from NLP_25 import get_fund_infomation


def remove_markup(fund):
    pattern1 = re.compile(r"\'{2,5}", re.MULTILINE)  # remove '''
    pattern2 = re.compile(r"\[\[(.+?)\]\]", re.MULTILINE)  # remove [[]]
    for key, value in fund.items():
        fund[key] = pattern1.sub("", value)
        fund[key] = pattern2.sub(r"\1", fund[key])

    return fund


if __name__ == "__main__":
    fund = remove_markup(get_fund_infomation())
    for key, value in fund.items():
        print(key + ":" + value)
