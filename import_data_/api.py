#以http://www.omdbapi.com/为例
#在网站上申请api后会得到key

#my key: abb2ffe

#eg:OMDb API: http://www.omdbapi.com/?i=tt3896198&apikey=abb2ffe

import requests
import pickle

#1、基础操作
'''
#write url according to the example given by API website,and dont forget the key
#search by id
url='http://www.omdbapi.com/?i=tt3896198&apikey=abb2ffe'

#search by name
url1='http://www.omdbapi.com/?t=Guardians+of+the+Galaxy+Vol.+2&apikey=abb2ffe'

# get response
r=requests.get(url)
r1=requests.get(url1)

#print response
dic=r.text
dic1=r1.text
print(dic)
print(dic1)
'''




#2
'''
#通过ID扫描抓取数据
#建立IDlist，用于组合ID
IDlist=['tt3896198']
for i in range(1,5):
    ID=3896198
    idnew=ID+i
    idnew=str(idnew)
    IDnew='{0}{1}'.format('tt',idnew)
    IDlist.append(IDnew)

#将ID与URL组合成URLlist
URLlist=[]
for i in IDlist:
    URLlist.append('{0}{1}{2}'.format('http://www.omdbapi.com/?i=',i,'&apikey=abb2ffe'))

#请求并写入pickle文件
file=open('omdb.pkl','wb+')
for i in URLlist:
    r=requests.get(i)
    omdb_data=r.text
    pickle.dump(omdb_data,file)
'''



#3调用维基百科的api
'''
# Import package
import requests

# Assign URL to variable: url
url='https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data=r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)
'''




#4 Twitter API(需要账号）

import json,tweepy
#需要申请
# Import package
import tweepy   #twitter的API
import re
import matplotlib.pyplot as plt
import seaborn as sns

# Store OAuth authentication credentials in relevant variables
access_token = "792925111896596480-JRgUa4qwg68IpV8yRobbpGJNPD8ZsT5"
access_token_secret = "5Y8kip7yeiEcoB4LPeXonzWC2WwPh5or2I6VSWLoy7Pnm"
consumer_key = "sUcpTNvWoLK8qrRtVwZjB4TVT"
consumer_secret = "qlNdXCiC1WJLqRM2Gn7eOdHf81ZXjYqDN5FFD2MEXdutkOihX0"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#test
#api = tweepy.API(auth)
#for status in tweepy.Cursor(api.home_timeline).items(2):
#    print (status.text)

#define stream listener class
class  MyStreamListener(tweepy.StreamListener):
    def __init__(self,api=None):
        super(MyStreamListener,self).__init__()  #继承
        self.num_tweets = 0   #初始化Tweets的数量
        self.file=open('tweets.txt','w+')  #创建本地文件

    def on_status(self,status):
        tweet_list = []
        tweet=status._json
        self.file.write(json.dumps(tweet)+'\n') #将返回值写入json
        tweet_list.append(status) #接受twitter的返回值
        self.num_tweets += 1
        if self.num_tweets<100:  #请求十次数据
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False

#实例化
l=MyStreamListener
stream=tweepy.Stream(auth,l())

#根据关键字在twitter上提取数据
stream.filter(track=['Refugee','Germany','France'])  #不要有特朗普、克林顿等查询，会返回空


#读取
# String of path to file: tweets_data_path
tweets_data_path='tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data=[]

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet=json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
#print(tweets_data)



#作图
#使用pandas将数据转化为DataFrame
import pandas as pd

#查看保存的json文件是否为空
json_file=open('tweets.txt','r')
if json_file==None:
    print('false')
    pass

#读取json并转化为dict，之后导入pandas的DataFrame
datalist=[json.loads(line) for line in json_file]
df=pd.DataFrame(datalist)

#计数
[Refugee, Germany, France] = [0,0,0]

#统计次数
def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, text)

    if match:
        return True
    return False


for index,row in df.iterrows():
   Refugee+=word_in_text('refugee',row['text'])
   Germany+=word_in_text('germany',row['text'])
   France += word_in_text('france', row['text'])




# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['refugee', 'Germany', 'France']

# Plot histogram
ax = sns.barplot(cd,[Refugee, Germany, France] )
ax.set(ylabel="count")
plt.show()