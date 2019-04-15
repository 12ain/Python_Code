import requests as re
from bs4 import BeautifulSoup
r = re.get("http://www.baidu.com")
r.encoding = 'utf-8'
print(r.text)
soup = BeautifulSoup(r.text)
print(soup.find_all('a'))
