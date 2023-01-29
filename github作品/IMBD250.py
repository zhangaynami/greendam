# -*- codeing = utf-8 -*-
import requests
import pandas as pd
from lxml import etree
import time
import json
imbd_250 = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
ua = { "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

# user_num = int(input("请输入要提取的排名数"))
get_web = requests.get(url = imbd_250,headers = ua).text
# print(get_web)
get_data = etree.HTML(get_web)
# print(get_data)
movie_title = get_data.xpath('//td[@class="titleColumn"]/a/text()')
movie_year = get_data.xpath('//td[@class="titleColumn"]/span/text()')
movie_score = get_data.xpath('//td[@class="ratingColumn imdbRating"]/strong/text()')
movie_link = get_data.xpath('//td[@class="titleColumn"]/a/@href')
all_links =[]
for i in movie_link:
    all_link = 'https://www.imdb.com' + i
    all_links.append(all_link)
mov_data = pd.DataFrame({"电影名称": movie_title, "上映时间": movie_year, "评分": movie_score,"详情":all_links})
mov_data.index = mov_data.index + 1
mov_data.to_excel("D:/PYTHONSTUDY/pythonProject7/实战/imbd250A.xlsx")
# for i in range(0,user_num):
#
#     li = 'https://www.imdb.com' + movie_link[i] #详情网址
#     get_movie =  requests.get(url = li ,headers = ua).text
#     get_movie_data = etree.HTML(get_movie)
#
#     movie_hours = get_movie_data.xpath('//div[@class="sc-5be2ae66-2 jaKsxz"]//li[@role="presentation"]/text()') #影片时长
#
#     movie_directors = get_movie_data.xpath('/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section[4]/ul/li[1]/div/ul/li/a/text()')#导演
#     # movie_d = ';'.join(movie_directors)
#     movie_gens = get_movie_data.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div/div[2]/a/span/text()')#类型
#     # movie_g = ';'.join(movie_gens)
#     mov_data = pd.DataFrame({"导演":movie_d,"类型":movie_g,"影片时长":movie_hours,"详情":li})
#     print(movie_d)
#     mov_data.index = mov_data.index + 1
#     mov_data.to_excel("D:/PYTHONSTUDY/pythonProject7/实战/imbd2501.xlsx")
#     # mov_data.to_csv("D:/PYTHONSTUDY/pythonProject7/爬虫/250list.csv",index=False,header=0,mode='a',encoding='ANSI')
