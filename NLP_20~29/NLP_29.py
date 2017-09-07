# coding: utf-8
import re
import urllib.parse
import urllib.request
from NLP_25 import get_fund_infomation
from NLP_28 import remove_markup


def get_image(fund):
    name = fund['国旗画像']
    url = 'https://www.mediawiki.org/w/api.php?' \
        + 'action=query' \
        + '&titles=File:' + urllib.parse.quote(name) \
        + '&format=json' \
        + '&prop=imageinfo' \
        + '&iiprop=url'

    request = urllib.request.Request(url, headers={'User-Agent': 'ttakano'})
    connection = urllib.request.urlopen(request)
    data = json.loads(connection.read().decode())
    return data['query']['pages'].popitem()[1]['imageinfo'][0]['url']


if __name__ == "__main__":
    fund = remove_markup(get_fund_infomation())
    print(get_image(fund))


# URL取り出し
#url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
# print(url)
