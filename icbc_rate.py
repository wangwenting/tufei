#coding:utf-8
from bs4 import BeautifulSoup

import util

icbc_url = "http://www.icbc.com.cn/ICBCDynamicSite2/other/rmbdeposit.aspx"

def get_dates(url):
    soup = BeautifulSoup(util.get(url, None))
    options = soup.findAll("option")

    dates = []
    for option in options:
        option_value = option.get_text()
        if not option_value.find(u"选择") > 0:
           dates.append(option_value) 
    return dates

def get_VIEWSTATE(url):
    soup = BeautifulSoup(util.get(url, None))
    data = soup.find("input", attrs={"name": "__VIEWSTATE"})
    return data["value"]
    

def get_datas(url):
    viewstate = get_VIEWSTATE(url)
    dates = get_dates(url)
    all_datas={}

    for date_v in dates:
        post_datas = {}
        post_datas["Sel_Date"] = date_v
        post_datas["__VIEWSTATE"] = viewstate
        soup = BeautifulSoup(util.post(url, post_datas))
        tbody = soup.find("tbody")
        trs = tbody.findAll("tr")
        for tr in trs:
            if tr.get_text().find(u"活期") > 0:
                tds = tr.findAll('td')
                all_datas[date_v] = tds[1].get_text()
    return all_datas

if __name__ == "__main__":
    datas = get_datas(icbc_url)
    sort_datas = [(k,datas[k]) for k in sorted(datas.keys())]
    for sort_data in sort_datas:
        print sort_data
