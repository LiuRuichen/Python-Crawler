from bs4 import BeautifulSoup
import requests
import os

URL = r'https://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

page = requests.get(url = URL, headers = headers)
page.encoding = 'utf-8'
soup = BeautifulSoup(page.text, 'lxml') #实例化BeautifulSoup对象

a_list = soup.select('.book-mulu > ul > li > a')  #获取a标签

if not os.path.exists(r'C:\Users\未央\Desktop\三国演义'):
    os.mkdir(r'C:\Users\未央\Desktop\三国演义')

for a in a_list:
    title = a.string
    detail_URL = 'https://www.shicimingju.com' + a['href']
    detail_page = requests.get(url = detail_URL, headers = headers)
    detail_page.encoding = 'utf-8'
    #解析出详情页中相关章节
    detail_soup = BeautifulSoup(detail_page.text, 'lxml')
    div_tag = detail_soup.find('div', class_ = 'chapter_content')
    content = div_tag.text
    
    with open('C:\\Users\\未央\\Desktop\\三国演义\\' + title + '.txt', 'w', encoding = 'utf-8') as fp:
        fp.write(content)
        
    print(title + '下载完成！')

