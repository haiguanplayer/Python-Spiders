'''
twitter
from twitter import Twitter

t = Twitter(auth=lllhaiguan("Access Token","Access Token Secret","Consumer Key","Consumer Secret"))
pythonTweets = t.search.tweets(q = "#python")
print (pythonTweets)
'''
from twitter import Twitter

#Make sure to add the access tokens and consumer keys for your application
t = Twitter(auth=("Access Token","Access Token Secret","Consumer Key","Consumer Secret"))
pythonTweets = t.search.tweets(q = "#python")
print(pythonTweets)