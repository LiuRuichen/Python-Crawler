
'''
爬虫的四个步骤
1. 指定url
2. 发起请求
3. 获取响应数据
4. 存储响应数据
'''
'''
在真正爬取数据的时候需要进行User-Agent伪装，
相当于当前请求载体伪装成了一个浏览器。因为门户网站会检测载体身份标识，
如果载体是一个浏览器则代表是一个正常的请求，服务器端一般不会拒绝。但是，
如果不是一个浏览器，则服务器认为是一个不正常的请求，很可能会拒绝，
所以我们需要伪装成一个浏览器。
'''

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 23:39:39 2021
"""
import requests
import json

URL = "https://fanyi.baidu.com/sug"

word = input('Enter a word:')

data = {
    "kw": word
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

response = requests.post(url = URL, data = data, headers = headers)

dic_obj = response.json()

print(dic_obj)

file_name = 'C://Users//未央//Desktop//' + word + '.json'
fp = open(file_name, 'w', encoding = 'utf-8')  
json.dump(dic_obj, fp = fp, ensure_ascii = False)

fp.close() #不关闭的话文件可能为空

print('over')

