import requests
import time


def getHTMLText(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = 'utf-8'
		return r.text
	except:
		return ""


url = "http://www.baidu.com"
totaltime = 0
for i in range(100):
	starttime = time.perf_counter()
	getHTMLText(url)
	endtime = time.perf_counter()
	totaltime = totaltime + endtime - starttime
print("爬取100次用了{}秒".format(totaltime))
