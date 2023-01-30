# -*- codeing = utf-8 -*-
import requests
import re
import pandas as pd
import csv
page = 0
while page <= 225:
    douban250 = f'https://movie.douban.com/top250?start={page}&filter='
    ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    get_web = requests.get(url = douban250,headers = ua).text
    # print(get_web)
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                     r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                     r'.*?<span>(?P<num>.*?)</span>'

                     ,re.S)
    # print(obj)
    request = obj.finditer(get_web)

    for i in request:
        # na = (i.group('name'))
        # ye = (i.group('year').strip())
        # sc = (i.group('score'))
        # nu = (i.group('num').strip())
        # print(na,ye,sc,nu)
        dic = i.groupdict() #组成字典
        dic['year'] =  dic['year'].strip()

        print(dic)
        down_link = 'D:/PYTHONSTUDY/pythonProject7/爬虫/re模块/top250.csv'
        download = pd.DataFrame(dic,index=[0])
        download.to_csv(down_link,mode='a',header=0,index=False,encoding='ANSI')
    page = page + 25