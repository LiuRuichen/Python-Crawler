from lxml import etree
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

URL = r'https://www.aqistudy.cn/historydata/'
res = requests.get(url = URL, headers = headers)
res.encoding = 'utf-8'

page_text = res.text

tree = etree.HTML(page_text)

cities_list = tree.xpath('//div[@class="hot"]//ul/li/a | //div[@class="bottom"]/ul/div[2]//a')

fp =  open (r'C:\Users\未央\Desktop\全国城市名称.txt', 'w')

a_list = tree.xpath('//div[@class="hot"]//ul/li/a')
fp.write('热门城市: ')  
for a in a_list:
    name = a.xpath('./text()')
    if a == a_list[-1]:
        fp.write(name[0] + '\n')
    else:
        fp.write(name[0] + ', ')  
            
ul_list = tree.xpath('//div[@class="all"]//ul')  

for ul in ul_list:
    initial = ul.xpath('./div[1]/b/text()')
    fp.write('以' + initial[0][0] + '字母为首的城市: ')
    cities_names = ul.xpath('./div[2]//a')
    for names in cities_names:
        if names == cities_names[-1]:
            fp.write(names.xpath('./text()')[0] + '\n')
        else:
            fp.write(names.xpath('./text()')[0] + ', ') 

city_set = []
for city in cities_list:
    city_set.append(city.xpath('./text()')[0])

city_set = set(city_set)

fp.write('共计' + str(len(city_set)) + '个城市。')  #需要去重，列表转集合来去重

fp.close()                    