import ast

import requests
import csv
import re

f=open('data.csv', mode='w', encoding='utf-8-sig', newline='')
csv_writer=csv.DictWriter(f,fieldnames=['昵称','归属地','点赞','性别','内容'])
csv_writer.writeheader()
def get_content(max_id):
    headers={
        'Cookie':'SUB=_2AkMS2eGif8NxqwFRmfoWyWjrb4t3wwzEieKkhRB5JRMxHRl-yT9kqmkotRB6OVnPTVcwXH2MTmjuC1rIeQxm6JrYl0m_; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFpC6Ia0zbgFv6l9FiDvIhQ; XSRF-TOKEN=gPbTpd6D9Kr8GY-nrFjmg9sV; WBPSESS=V0zdZ7jH8_6F0CA8c_ussesUUeuBWcFNA6IrLt7bffaArULSut-2Gx9z9hiOWkkATNqTQZ_R3SK5mhYDYxcy9Ak0h2CQxotOPADyRoIXfTllEpOWWCk1X7wfvrAJSikW1am9khogLEOl97XQx6B7yFSNFWkT3n-hgZ2WrVLFyOo=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    #请求网址
    url=f'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4988935608729791&is_show_bulletin=2&is_mix=0&max_id={max_id}&count=10&uid=1566301073&fetch_level=0&locale=zh-CN'
    #请求参数
    response= requests.get(url=url,headers=headers)
    json_data=response.json()
    info_list=json_data['data']
    for index in info_list:
        name=index['user']['screen_name']
        ip=index['source'].replace('来自','')
        content=re.sub(r'http\S+', '', index['text_raw'])
        like=index['like_counts']
        #性别处理
        if index['user']['gender']=='f':
            sex='女'
        elif index['user']['gender']=='m':
            sex='男'
        else:
            sex='保密'
        dit= {
            '昵称': name,
            '归属地': ip,
            '点赞': like,
            '性别': sex,
            '内容': content,
        }
        csv_writer.writerow(dit)
        print(name,sex,ip,content,like)
    max_id=json_data['max_id']
    return max_id
max_id=''
for page in range(1,21):
    max_id=get_content(max_id)