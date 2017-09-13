from urllib import request
from bs4 import BeautifulSoup
import re
import sys

file = open('一念永恒.txt', 'w', encoding='utf-8')

def download(url,index,num):
    # User-Agent
    head = {}
    head[
        'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    download_req = request.Request(url=url, headers=head)
    download_response = request.urlopen(download_req)
    download_html = download_response.read().decode('gbk', 'ignore')
    download_name = child.string
    soup_texts = BeautifulSoup(download_html, 'lxml')
    texts = soup_texts.find_all(id='content', class_='showtxt')
    soup_text = BeautifulSoup(str(texts), 'lxml')
    write_flag = True
    file.write(download_name + '\n\n')
    # 将爬取内容写入文件
    for each in soup_text.div.text.replace('\xa0', ''):
        if each == 'h':
            write_flag = False
        if write_flag == True and each != ' ':
            file.write(each)
        if write_flag == True and each == '\r':
            file.write('\n')
    file.write('\n\n')
    # 打印爬取进度
    sys.stdout.write("已下载:%.3f%%" % float(index / num) + '\r')
    sys.stdout.flush()

if __name__ == "__main__":
    url = 'http://www.biqukan.com/1_1094/'
    #User-Agent
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url = url, headers = head)
    response = request.urlopen(req)
    html = response.read().decode('gbk','ignore')
    #创建BeautifulSoup对象
    listmain_soup = BeautifulSoup(html, 'lxml')
    #找出div标签中class为listmain的所有子标签
    chapters = listmain_soup.find_all('div',class_ = 'listmain')
    #在创建一个BeautifulSoup对象，用来解析
    download_soup = BeautifulSoup(str(chapters),'lxml')
    #计算章节个数
    num = (len(download_soup.dl.contents) - 1) / 2 - 8;
    index = 1
    #只要正文内容
    flag = False
    #遍历dl标签下所有子节点
    for child in download_soup.dl.children:
        #滤出回车符
        if child == "\n":
            continue
        #找到正文
        if child.string == u"《一念永恒》正文卷":
            flag = True
        #爬取链接
        if flag == True and child.a != None:
            download_url = "http://www.biqukan.com/"+child.a.get('href')
            #下载函数
            download(download_url,index,num)
            index += 1
    file.close()