import json
#适用德国使馆在线签证申请表填写系统生成的json
with open('visa.json','r') as json_file:
    jsondata_visa=json.load(json_file)

for key in jsondata_visa:
    print('{0}:{1}'.format(key,jsondata_visa[key]))


#调用API，并转化为字典
# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=ff21610b&t=social+network'

# Package the request, send the request and catch the response: r
r=requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data=r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])