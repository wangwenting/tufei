#coding:utf-8
import icbc_rate
import zgjh_rate
import json

zgjh_url = "http://www.ccb.com/cn/personal/interestv3/rmbdeposit.html"
icbc_url = "http://www.icbc.com.cn/ICBCDynamicSite2/other/rmbdeposit.aspx"
path = "/Users/wangwenting/money_rate.txt"


def write_file(path, datas):
    lengh = len(datas)
    value = []
    for i in range(lengh):
      val = {}
      if i < (lengh-1):
          val["start_time"] = datas[i][0]
          val["end_time"] = datas[i+1][0]
          val["value"] = datas[i][1]
      else:
          val["start_time"] = datas[i][0]
          val["end_time"] = "2100-10-11"
          val["value"] = datas[i][1]
      value.append(val)
    value_str = json.dumps(value)
    with open(path, 'w') as f:
        f.write(value_str)

if __name__ == "__main__":
    datas = zgjh_rate.get_datas(zgjh_url)
    sort_datas = []
    if datas:
        sort_datas = [(k,datas[k]) for k in sorted(datas.keys())] 
    else:
        datas = icbc_rate.get_datas(icbc_url)
        if datas:
            sort_datas = [(k,datas[k]) for k in sorted(datas.keys())] 
    if sort_datas:
        write_file(path, sort_datas)
    else:
        #todu send 报警
        pass
