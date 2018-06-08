import pandas as pd
from sqlalchemy import engine
from urllib.request import urlretrieve
import matplotlib.pyplot as plt
#抓取网络数据

'''
#1、urllib
#抓取红酒数据库并保存在本地

# Assign url of file: url
url='https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url,'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')


# Print the head of the DataFrame
print(df.head())

# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])  #df.ix 是loc 及 iloc的混用
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()
'''



'''
#2、读取在线excel
# Import package
import pandas as pd
from urllib.request import urlretrieve
# Assign url of file: url
url='http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xl
xl=pd.read_excel(url,sheetname=None)

# Print the sheetnames to the shell
print(xl.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xl['1700'].head())
'''



'''
#3、运用urllib中的Request和responce在python中打印http request
## Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request
request = Request(url)  #将url打包，做成请求

# Sends the request and catches the response: response
response=urlopen(request)  #接受回复

# Extract the response: html
html=response.read()   #读取

# Print the html
print(html)  #打印

# Be polite and close the response!
response.close()   #结束
'''


'''
#4 运用requests包完成3的目标
import requests

url='http://www.datacamp.com/teach/documentation'

#请求并受到回复
response=requests.get(url)
text=response.text
#打印
print(text)
'''
