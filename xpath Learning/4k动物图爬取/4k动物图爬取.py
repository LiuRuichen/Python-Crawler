from lxml import etree
import requests
import os

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

if not os.path.exists(r'C:\Users\未央\Desktop\4k动物图'):
    os.mkdir(r'C:\Users\未央\Desktop\4k动物图')

for idx in range(1,22):
    if idx == 1:
        URL = r'https://pic.netbian.com/4kdongwu/'
    else: 
        URL = r'https://pic.netbian.com/4kdongwu/index_' + str(idx) + '.html'  
        
    page = requests.get(url = URL, headers = headers)
    page.encoding = 'gbk'
    page_text = page.text

    #数据解析
    tree = etree.HTML(page_text)
    li_list  = tree.xpath('//div[@class="slist"]//li')
    
    if not os.path.exists('C:\\Users\\未央\\Desktop\\4k动物图\\第' + str(idx) + '页'):
        os.mkdir('C:\\Users\\未央\\Desktop\\4k动物图\\第' + str(idx) + '页')
    
    current_path = 'C:\\Users\\未央\\Desktop\\4k动物图\\第' + str(idx) + '页'
    
    for li in li_list:
        img_url = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'

        res = requests.get(url = img_url, headers = headers).content

        with open(current_path + '\\' + img_name, 'wb') as fp:
            fp.write(res)
    
    print('第' + str(idx) + '页爬取完毕！')