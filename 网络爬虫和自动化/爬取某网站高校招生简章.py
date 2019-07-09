import requests
import re
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""

def getAllUrl():   # 总共所有大学的总页数
    allPageUrl = []
    urlFront = 'https://gaokao.chsi.com.cn/zsgs/zhangcheng/listVerifedZszc--method-index,lb-1,start-'
    urlback = '.dhtml'
    for i in range(0, 2900, 100):
        urlFull = urlFront + str(i) + urlback
        allPageUrl.append(urlFull)
    return allPageUrl

def getSingleUrl():   #获取每页大学的列表及连接
    allurl = getAllUrl()
    singleUrl = []
    for i in range(len(allurl)):
        url = allurl[i]
    # print(url)
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        urllist = soup.find_all(href=re.compile("^/zsgs/zhangcheng/listZszc"))
    # print(listurl)
    # urlname = []                                # 保存所有院校名称备用
        if urllist != []:
            for i in range(len(urllist)):
            # urlname.append(urllist[i].string)
                singleUrl.append('https://gaokao.chsi.com.cn/'+urllist[i]['href'])
    print(len(singleUrl))
    return singleUrl

def everyUrl():
    finalurls = []
    finalname = []
    allUrl = getSingleUrl()
    for i in range(len(allUrl)):
        url = allUrl[i]
    # print(url)
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        everyUrl = soup.find_all('a', class_='ablue')
        if everyUrl != []:
            finalurls.append('https://gaokao.chsi.com.cn/'+everyUrl[0]['href'])
            finalname.append(everyUrl[0].string)
        # print(finalurls)
    # print(len(finalurls))
    # print(finalurls)
    print(finalname)
    return finalurls, finalname




def ProcessData():   # 对每页数据进行爬取并保存
    urls, finalname = everyUrl()
    for i in range(len(urls)):
    # url = 'https://gaokao.chsi.com.cn/zsgs/zhangcheng/listVerifedZszc--infoId-2347484040,method-view,schId-119.dhtml'
        url = urls[i]
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        text = soup.find_all('div', class_="content")
        if text != []:
            print(text[0].text)
            fname = '爬取数据/' + str(finalname[i]) + '.doc'
            fo = open(fname, "w+", encoding="utf-8")
            ls = text[0].text
            fo.writelines(ls)
            for line in fo:
                print(line)
            fo.close()

ProcessData()
# getSingleUrl()
# everyUrl()
