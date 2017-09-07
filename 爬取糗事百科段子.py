'''
爬虫实例
爬取糗事百科中的段子
'''
import urllib
import urllib.request
import rehttps:

class QSBK():
    def __init__(self):
        self.url = 'http://www.qiushibaike.com/hot/page/'
        self.user_agent = 'Mozilla/4.0(cpmpatible;MSIE 5.5;Windows NT)'
        self.headers = {'User-Agent':self.user_agent}
        self.story_num = 0
        self.stories = []
    #请求函数
    def request(self,page):
        request = urllib.request.Request(self.url+str(page),headers=self.headers)
        response = urllib.request.urlopen(request)
        return response.read().decode('utf-8')#将页面转化为UTF-8编码

    #将获取到的网页和正则表达式进行匹配并返回匹配到的每个段子的信息列表
    def getOnePage(self,content):
        try:
            pattern = re.compile('<.*?class="author.*?>.*?<a.*?<h2>(.*?)</h2>.*?<div.*?class="content".*?<span>(.*?)</span>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
            self.stories.append(re.findall(pattern, content))     #将获取到的每一页的段子追加到存储列表中
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
    #开始
    def start(self):
        num = input("输入你想要进行爬取的页数:")
        for i in range(int(num)):
            content = self.request(i+1)
            self.getOnePage(content)

        print("输出段子:")
        page = 1
        print("每按一次快捷键读取一条段子,按Q退出！")
        for all in self.stories:#访问每页
            print("第%d页："%page)
            for item in all:#输入每个无图的段子
                self.story_num += 1
                next = input()
                if next == 'Q':#输入Q截止
                    return
                if not re.search('img',item[2]):
                    i += 1
                    print("第%d个段子: "%self.story_num+"作者:"+str(item[0]),"内容:"+str(item[1])+"点赞人数:"+str(item[3]))
            page += 1
        print("段子输出完毕！")

qiushibaike=QSBK()
qiushibaike.start()