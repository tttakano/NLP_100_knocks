# -*- coding: utf-8 -*-
import re
from NLP_25 import get_fund_infomation


def remove_markup(fund):
    pattern1 = re.compile(r"\'{2,5}", re.MULTILINE)  # remove '''
    pattern2 = re.compile(r"\[\[(.+?)\]\]", re.MULTILINE)  # remove [[]]
    pattern3=re.compile(r"\{\{lang(?:[^|]*?\|)*?([^|]*?)\}\}", re.MULTILINE)  # {{lang|言語タグ|文字列}}
    pattern4=re.compile(r"\[.*?\s(.*?)\]", re.MULTILINE)  # [http://www.example.org 表示文字]
    pattern5=re.compile(r"<\/?[ref|br][^>]*?>", re.MULTILINE)  # [http://www.example.org 表示文字]
    for key, value in fund.items():
        fund[key] = pattern1.sub("", value)
        fund[key] = pattern2.sub(r"\1", fund[key])
        fund[key] = pattern3.sub(r"\1", fund[key])
        fund[key] = pattern4.sub(r"\1", fund[key])
        fund[key] = pattern5.sub("", fund[key])
    return fund

if __name__ == "__main__":
    fund = remove_markup(get_fund_infomation())
    for key, value in fund.items():
        print(key + ":" + value)
