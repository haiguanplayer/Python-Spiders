'''
获取淘宝的接口
要实现翻页request-re
'''
import requests
import re

def getHTMLText(url):#获得网页内容
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt,html):#解析页面
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)#价格信息
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)#名称等
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
            print("")
def printGoodsList(ilt):#输出商品列表
    tplt = "{:4}\t{:8}\t{:16}"#长度分别为4，8，16
    print (tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print (tplt.format(count,g[0],g[1]))
def main():
    goods = "书包"
    depth = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i);
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)
main()
