#coding:utf-8
from bs4 import BeautifulSoup

import util

def get_rate(key, url):
    datas={}
    soup_rate = BeautifulSoup(util.get(url, None))
    trs = soup_rate.findAll('tr')
    for tr in trs:
        if tr.get_text().find(u"活期") > 0:
            tds = tr.findAll('td')
            datas[key] = tds[1].get_text()
    return datas

soup = BeautifulSoup(util.get("http://www.ccb.com/cn/personal/interestv3/rmbdeposit.html",None))

summary = soup.find("div", attrs={"class": "qur_r"})

lis = summary.findAll('li')

for li in lis:
    key = li.get_text()
    data = li["data"].replace("@","_")
    url = "http://www.ccb.com/cn/personal/interestv3/%s.html" % data
    datas = get_rate(key, url) 
    for d, value in datas.items():
        print d, value
