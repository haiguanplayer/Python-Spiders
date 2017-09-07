import urllib
import socket
import re
import BeautifulSoup
def getData(url, timeOut = 10):
    try:
        html = urllib.urlopen(url, timeout = timeOut)
        htmlData = html.read()
    except Exception as e:
        htmlData = None
    finally:
        return htmlData

for i in range(13124750, 131230000):
    c = getData("http://paste.ubuntu.com/"+str(i)+"/")

    #if re.search("#include", c):
    if c.find("#include") != -1:
        print(i)