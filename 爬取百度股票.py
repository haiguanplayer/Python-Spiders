import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url,code = 'utf-8'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""
def getStockList(lst,stockURL):#获取股票的url列表
    html = getHTMLText(stockURL,'GB2312')
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            #检索s开头，中间h/z，后面6个数字
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue
    return ""
def getStockInfo(lst,stockURL,fpath):#获取股票的信息列表
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}#字典
            soup = BeautifulSoup(html,'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})
            keyList = stockInfo.find_all('dt')#键
            valueList = stockInfo.find_all('dd')#值
            for i in range(len(keyList)):
                key = keyList[i].text
                value = valueList[i].text
                infoDict[key] = value
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count += 1
                print ('\r当前速度: {:.2f}%'.format(count*100/len(lst)),end='')
        except:
            count += 1
            print('\r当前速度: {:.2f}%'.format(count * 100 / len(lst)), end='')
            continue
def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'F://BaiduStockInfo.txt'
    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)
main()