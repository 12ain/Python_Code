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


def getUrl(choice):
    url1 = 'http://124.117.250.18/ptjh/y_jhqr/g_leftframe.php?yzdm=01&pcdm=1'  # 一本院校列表
    url2 = 'http://124.117.250.18/ptjh/y_jhqr/g_leftframe.php?yzdm=01&pcdm=2'  # 二本院校列表
    url3 = 'http://124.117.250.18/ptjh/y_jhqr/g_leftframe.php?yzdm=01&pcdm=5'  # 高职(专科)列表
    front = 'http://124.117.250.18/ptjh/y_jhqr/'
    urlList = []
    schoolList = []
    if choice == '1':
        urlText = getHTMLText(url1)  # 选择抓取的批次
    elif choice == '2':
        urlText = getHTMLText(url2)  # 选择抓取的批次
    elif choice == '3':
        urlText = getHTMLText(url3)  # 选择抓取的批次
    else:
        return ''
    soupp = BeautifulSoup(urlText, "html.parser")
    for urldata in soupp.find_all('a'):
        urlList.append(front + urldata['href'])
        schoolList.append(urldata.string)
    return urlList, schoolList


def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd) == 0:
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)
        for i in range(len(singleUniv)):
            if singleUniv[i] is not None:
                singleUniv[i] = singleUniv[i].strip()
            else:
                singleUniv[i] = ''
        # singleUniv[i].replace(' ', '')
        # print(singleUniv)
        allUniv.append(singleUniv)


def outputUnivList(allUniv, schoolName):
    allUniv.pop(0)
    allUniv.pop(-1)
    allUniv.pop(0)
    allUniv.pop(0)
    output = open('data.xls', 'a', encoding='gbk')
    for i in range(len(allUniv)):
        allUniv[i].insert(0, schoolName)
        for j in range(len(allUniv[i])):
            output.write(str(allUniv[i][j]))  # write函数不能写int类型的参数，所以使用str()转化
            output.write('\t')                # 相当于Tab一下，换一个单元格
        output.write('\n')                    # 写完一行立马换行
    output.write('\n')
    output.close()

def main():
    chose = input('请输入要爬取的批次:(一本输入1,二本输入2,专科输入3)')
    urlList, schoolList = getUrl(chose)
    for i in range(len(urlList)):
    # for i in range(5):
        url = urlList[i]
        schoolName = schoolList[i]
        # print(url)
        print(schoolName)
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        fillUnivList(soup)
        outputUnivList(allUniv, schoolName)
        allUniv.clear()

main()
