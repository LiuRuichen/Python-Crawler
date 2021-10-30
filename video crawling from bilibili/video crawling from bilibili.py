import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'referer': 'https://www.bilibili.com/video/BV1H44y1t75x/'}

#网页URL
URL = r'https://www.bilibili.com/video/BV1H44y1t75x/'

#音频文件
URL_30280 = r'https://cn-gddg-cmcc-v-05.bilivideo.com/upgcxcode/58/17/423711758/423711758_nb2-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1635606720&gen=playurlv2&os=vcache&oi=1971855785&trid=000125fbc0a8dc904107a73eaeba0560e2c6u&platform=pc&upsig=1966e7e1d39f7e493ef0e2b789e05d7b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&cdnid=2125&mid=0&bvc=vod&nettype=0&orderid=0,3&agrr=0&logo=80000000'

#视频文件
URL_30033 = r'https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/58/17/423711758/423711758-1-30033.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1635606720&gen=playurlv2&os=hwbv&oi=1971855785&trid=25fbc0a8dc904107a73eaeba0560e2c6u&platform=pc&upsig=b202fe092c63e61c058ad929a28566a2&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&bvc=vod&nettype=0&orderid=0,3&agrr=0&logo=80000000'

#解析视频名称
URL_text = requests.get(url = URL, headers = headers).text
tree = etree.HTML(URL_text)
file_name = tree.xpath('//div[@class="l-con"]//h1/@title')[0]

#解析音频文件
res_30280 = requests.get(url = URL_30280, headers = headers).content
with open (r'C:\Users\未央\Desktop\爬取音频_30280.mp3', 'wb') as fp:
    fp.write(res_30280)
    
#解析视频文件
res_30033 = requests.get(url = URL_30033, headers = headers).content
with open (r'C:\Users\未央\Desktop\爬取视频_30033.mp4', 'wb') as fp:
    fp.write(res_30033)

#在外部使用ffmpeg进行视频和音频的合成
    
print(file_name + '.mp4' + '爬取完毕！')
