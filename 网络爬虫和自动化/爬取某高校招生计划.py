import requests
import re
from bs4 import BeautifulSoup

allUniv = []


def getHTMLText(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = 'utf-8'
		return r.text
	except:
		return ""


def fillUnivList(soup):
	data = soup.find_all('tr')
	for tr in data:
		ltd = tr.find_all('td')
		if len(ltd) == 0:
			continue
		singleUniv = []
		for td in ltd:
			singleUniv.append(td.string)
		allUniv.append(singleUniv)


def main(num):
	url = 'http://124.117.250.18/ptjh/y_jhqr/g_gbjhyxjh.php?yzdm=01&pcdm=2&yxdh=1052&yxmc=1052上海海关学院'
	html = getHTMLText(url)
	soup = BeautifulSoup(html, "html.parser")
	fillUnivList(soup)
	# ls = re.findall()replace( / (^ \s *) | (\s * $) / g, "")
	print(allUniv)


# printUnivList(num)

main(10)
