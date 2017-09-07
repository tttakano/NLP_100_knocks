# -*- coding: utf-8 -*-
import types
import json
import gzip
filename = "./files/jawiki-country.json.gz"


def get_data():
    with gzip.open(filename, 'r') as f:
        for line in f:
            obj = json.loads(line)
            if obj["title"].encode('utf-8') == "イギリス":
                return obj["text"].encode('utf-8')


if __name__ == "__main__":
    print(get_data())
