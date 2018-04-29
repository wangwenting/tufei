#coding:utf-8
from bs4 import BeautifulSoup

import util

zgjh_url = "http://www.ccb.com/cn/personal/interestv3/rmbdeposit.html"

def get_rate(key, url):
    soup_rate = BeautifulSoup(util.get(url, None))
    trs = soup_rate.findAll('tr')
    for tr in trs:
        if tr.get_text().find(u"活期") > 0:
            tds = tr.findAll('td')
            return tds[1].get_text()
    return None

def get_datas(url):
    
    soup = BeautifulSoup(util.get(url, None))
    summary = soup.find("div", attrs={"class": "qur_r"})
    datas = {}
    lis = summary.findAll('li')

    for li in lis:
        key = li.get_text()
        data = li["data"].replace("@","_")
        url = "http://www.ccb.com/cn/personal/interestv3/%s.html" % data
        value = get_rate(key, url) 
        datas[key] = value

    return datas


if __name__ == "__main__":
    datas = get_datas(zgjh_url)
    sort_datas = [(k,datas[k]) for k in sorted(datas.keys())]
    for sort_data in sort_datas:
        print sort_data
