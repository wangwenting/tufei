#coding:utf-8
import urllib
import urllib2


def urlopen(request):
    try:
        response = urllib2.urlopen(request)
        return response.read()
    except urllib2.HTTPError, e:
        print e.code
    except urllib2.URLError, e:
        print e.reason
    return None

def get(url, datas):
    request = None
    if datas:
        values = urllib.urlencode(datas) 
        geturl = url + "?" + values
        request = urllib2.Request(geturl)
    else:
        request = urllib2.Request(url)
    return urlopen(request)

def post(url, datas):
    values = urllib.urlencode(datas)
    request = urllib2.Request(url, values)
    return urlopen(request)

if __name__ == "__main__":
    print get("http://www.ccb.com/cn/personal/interestv3/rmbdeposit.html", None)
