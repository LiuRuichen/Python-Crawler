import requests
import os
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }

ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'

if not os.path.exists('C:\\Users\\未央\\Desktop\\糗图'):
        os.mkdir('C:\\Users\\未央\\Desktop\\糗图')
        
for no in range(1,14):
    
    URL = 'https://www.qiushibaike.com/imgrank/' + 'page/' + str(no) + '/'
        
    res = requests.get(url = URL, headers = headers).text #返回网页的html文件
    img_src = re.findall(ex, res, re.S)
    
    if not os.path.exists('C:\\Users\\未央\\Desktop\\糗图\\page ' + str(no)):
        os.mkdir('C:\\Users\\未央\\Desktop\\糗图\\page ' + str(no))

    for img in img_src: 
        addr = 'https:' + img
        print(addr)
        res = requests.get(url = addr, headers = headers).content #获取每张图片的地址
        #生成图片名称
        img_name = img.split('/')[-1]
        img_path = 'C:\\Users\\未央\\Desktop\\糗图\\page ' + str(no) + '\\' + img_name
    
        with open(img_path, 'wb') as f:
            f.write(res)
    print('第' + str(no) + '页下载完成')
    