'''
爬虫的四个步骤
1. 指定url
2. 发起请求
3. 获取响应数据
4. 存储响应数据
'''

import requests
import json

URL = "https://movie.douban.com/j/chart/top_list"

params = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

response = requests.get(url = URL, params = params, headers = headers)

list_data = response.json()

fp = open('C://Users//未央//Desktop//douban1.json', 'w', encoding = 'utf-8')  
json.dump(list_data, fp = fp, ensure_ascii = False)

fp.close() #不关闭的话文件可能为空

print('over')