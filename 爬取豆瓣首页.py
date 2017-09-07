'''
第一个爬虫示例：爬取
爬取豆瓣首页
'''

import urllib.request
#网址
url = "http://www.douban.com/"
#请求
request = urllib.request.Request(url)
#爬取结果
response = urllib.request.urlopen(request)

data = response.read()
#设置解码方式
data = data.decode('utf-8')
#输出
print(data)

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())