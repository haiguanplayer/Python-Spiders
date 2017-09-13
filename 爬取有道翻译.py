from urllib import request
from urllib import parse
import json

def translate(text):
    target_url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

    data = {}
    data['type'] = 'AUTO'
    data['i'] = text
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'true'

    data = parse.urlencode(data).encode('utf-8')
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(target_url,data,head)

    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    return target["translateResult"][0][0]["tgt"]

if __name__ == "__main__":
    print ("请输入要翻译的内容")
    text = input()
    result = translate(text)
    print ("%s"%result)