import re
import urllib.request
import urllib
import time

from collections import deque

head = {
     'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
     'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
 }
visited = set()
url = 'http://xlfans.com'  # 入口页面, 可以换成别的
data = None
full_url=urllib.request.Request(url,data,head)
urlop = urllib.request.urlopen(full_url)
data = urlop.read().decode('utf-8')
temp = re.search(r'href=\"http://xlfans.com/archives/(.{4})\" class=\"thumbnail\">(.*) alt=\"迅雷粉 (.*) 迅雷会员账号分享 共享中', data, re.M|re.I)
result = re.search(r'href=\"http://xlfans.com/archives/(.{4})', temp.group(), re.M|re.I)
url = url + "/archives/" + temp.group(1)
data = None
full_url=urllib.request.Request(url,data,head)
urlop = urllib.request.urlopen(full_url)
data = urlop.read().decode('utf-8')
save_path = 'D:\\Program Files\\python\\test.txt'
f_obj = open(save_path, 'w')
#获取系统时间，来判断是否为周末
cur_day = time.strftime("%w",time.localtime(time.time()))
if(cur_day == '5'):
    string = "迅雷粉周末迅雷会员账号"
elif cur_day == '6':
    string = "迅雷粉周末迅雷会员账号"
    print(cur_day)
else:
    string = "迅雷粉专享迅雷会员账号"
#娘的，是你逼我的
start = data.find(string)
data = data[start:]
data_que = data.split("</p>")
count = 0
for i in range(3):
    data_temp = data_que[i]
    num = -1
    acc_que = data_temp.split("<br />")
    for result in acc_que:
        num = num + 1
        if(count != 0):
            if(num == 0):
                continue
    f_obj.write(result)
    f_obj.write("\n")
    count = count + 1
f_obj.close()