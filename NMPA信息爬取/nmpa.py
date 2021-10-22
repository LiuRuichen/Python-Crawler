'''
爬虫的四个步骤
1. 指定url
2. 发起请求
3. 获取响应数据
4. 存储响应数据
'''

import requests
import pandas as pd

#1. 首先批量获取所有公司的ajax数据包中的ID值
URL = r'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList' #首页的ajax数据包的Request URL
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
id_list = [] #存储企业的id值
for page in range(1,51):
    page = str(page)
    data = {
        'on': 'true',
        'page': page,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': ''
        }
    res_id = requests.post(url = URL, data = data, headers = headers).json()
    for dic in res_id["list"]:
        id_list.append(dic["ID"])

#2. 获取企业详情数据
ltd_info_arr = []
index = []
post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for ID in id_list:
    data = {
        'id':ID
        }
    ltd_res = requests.post(url = post_url, data = data, headers = headers).json()  #这是一个字典类型
    ltd_info = {'企业名称':ltd_res['epsName'],
                '许可证编号':ltd_res['productSn'],
                '许可项目':ltd_res['certStr'],
                '企业住所':ltd_res['epsAddress'],
                '生产地址':ltd_res['epsProductAddress'],
                '社会信用代码':ltd_res['businessLicenseNumber'],
                '法定代表人':ltd_res['legalPerson'],
                '企业负责人':ltd_res['businessPerson'],
                '质量负责人':ltd_res['qualityPerson'],
                '发证机关':ltd_res['qfManagerName'],
                '签发人':ltd_res['xkName'],
                '日常监督管理机构':ltd_res['rcManagerDepartName'],
                '日常监督管理人员':ltd_res['rcManagerUser'],
                '有效期至':ltd_res['xkDate'],
                '发证日期':ltd_res['xkDateStr'],
                '状态':'正常',
                '投诉举报电话':'12331'
                }
    ltd_info_arr.append(ltd_info)
    index.append(ltd_res['epsName'])  #企业名称

df = pd.DataFrame(ltd_info_arr, index = index)
df.to_excel(r'C:\Users\未央\Desktop\info.xlsx')


