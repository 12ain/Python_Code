import requests
import re
from bs4 import BeautifulSoup
import numpy as np


allUniv = []


def getHTMLText(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = 'utf-8'
		return r.text
	except:
		return ""


def getUrl():
	url1 = 'http://124.117.250.18/ptjh/y_jhqr/g_leftframe.php?yzdm=01&pcdm=1'  # 一本院校列表
	url2 = 'http://124.117.250.18/ptjh/y_jhqr/g_leftframe.php?yzdm=01&pcdm=2'  # 二本院校列表
	url3 = 'http://124.117.250.18/ptjh/y_jhqr/g_leftframe.php?yzdm=01&pcdm=5'  # 高职(专科)列表
	front = 'http://124.117.250.18/ptjh/y_jhqr/'
	urlList = []
	urlText = getHTMLText(url1)  # 选择抓取的批次
	soupp = BeautifulSoup(urlText, "html.parser")
	for urldata in soupp.find_all('a'):
		urlList.append(front + urldata['href'])
	return urlList


def fillUnivList(soup):
	data = soup.find_all('tr')
	for tr in data:
		ltd = tr.find_all('td')
		if len(ltd) == 0:
			continue
		singleUniv = []
		for td in ltd:
			singleUniv.append(td.string)
		# print(type(singleUniv))
		for i in range(len(singleUniv)):
			if singleUniv[i] is not None:
				singleUniv[i] = singleUniv[i].strip()
			else:
				singleUniv[i] = ''
			# singleUniv[i].replace(' ', '')
		# print(singleUniv)
		allUniv.append(singleUniv)


def printUnivList():
	# print("{:^3}{:^10}{:^5}{:^8}{:^10}{:^12}{:^14}{:^16}".format('科类', '专业名称', '学制', '收费标准', '计划数', '计划性质及类别', '备注', '类别'))
	allUniv.pop(0)
	allUniv.pop(-1)
	allUniv.pop(0)
	allUniv.pop(0)
	return allUniv
	# for i in range(len(allUniv)):
		# u = allUniv[i]
		# print("{:^3}{:^10}{:^5}{:^8}{:^10}{:^12}{:^14}{:^16}".format(u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7]))


def outputUnivList():
	allUniv = printUnivList()
	output = open('data.xls', 'a', encoding='gbk')
	# output.write('科类\t专业名称\t学制\t收费标准\t计划数\t计划性质及类别\t备注\t类别\n')
	for i in range(len(allUniv)):
		for j in range(len(allUniv[i])):
			output.write(str(allUniv[i][j]))  # write函数不能写int类型的参数，所以使用str()转化
			output.write('\t')  # 相当于Tab一下，换一个单元格
		output.write('\n')  # 写完一行立马换行
	output.close()

def main():
	urlList = getUrl()
	# for i in range(len(urlList)):
	for i in range(5):
		url = urlList[i]
		# print(urlList[i])
	# url = urlList[0]
		print(url)
		html = getHTMLText(url)
		soup = BeautifulSoup(html, "html.parser")
		fillUnivList(soup)
		# printUnivList()
		outputUnivList()

main()
