# 2020.2.28
# 爬取某高校安全教育学习平台模拟题库
# 仅供学习交流
import requests
import re
from bs4 import BeautifulSoup

def getHTMLText(url,header):
    try:
        r = requests.get(url,headers=header, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def getText():
    questions = []
    answers = []
    urlText = getHTMLText('http://exam.sdsafeschool.gov.cn/m_mokao.php?',{"Cookie":''})# 此处填写Cookie
    soup = BeautifulSoup(urlText, "html.parser")
    # print(soup)
    question = soup.find_all("span", class_="title")
    for e in question:
        questions.append("".join(e.string.split()))
    answer = soup.find_all("span", id=re.compile(r'daan_'))
    for f in answer:
        answers.append("".join(f.string.split()))
    return questions,answers

def main():
    questions,answers = getText()
    for var1 in questions:
        print (var1)
    for var2 in answers:
        print (var2)

main()