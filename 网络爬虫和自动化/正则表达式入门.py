import re

# match = re.search(r'[1-9]\d{5}', 'BIT 100081')
# if match:
# 	print(match.group(0))


# match = re.match(r'[1-9]\d{5}', '100081 BIT')
# if match:
# 	print(match.group(0))


# ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
# print(ls)

import requests
from bs4 import BeautifulSoup
import traceback


def getHTMLText(url):
	return ""


def getStockList(lst, stockURL):
	return ""


def getStockInfo(lst, stockURL, fpath):
	return ""


def main():
	stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
	stock_info_url = 'https://gupiao.baidu.com/stock/'
	output_file = 'D://BaiduStockInfo.txt'
	slist = []
	getStockList(slist, stock_list_url)
	getStockInfo(slist, stock_info_url, output_file)


main()
