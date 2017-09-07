# -*- coding: utf-8 -*-
import re
from NLP_20 import get_data


def get_fund_infomation():
    data = get_data()
    pattern1 = re.compile(r"^{{基礎情報.*?$\n(.*?)^}}$", re.MULTILINE + re.DOTALL)
    pattern2 = re.compile(r"^\|(.*?)\s=\s(.+?)(?:(?=\n\|)|(?=\n$))", re.MULTILINE + re.DOTALL)
    result = pattern2.findall(pattern1.findall(data)[0])
    ans = {}
    for match in result:
        ans[match[0]] = match[1]
    return ans


if __name__ == "__main__":
    for key, value in get_fund_infomation().items():
        print(key + ":" + value)
