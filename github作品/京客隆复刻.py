# -*- codeing = utf-8 -*-
import requests
from lxml import etree
import pandas as pd

jkl_wb =  "https://www.jkl.com.cn/shop.aspx"
ua = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

visit_url = requests.get(url = jkl_wb,headers = ua).text
read_url = etree.HTML(visit_url)

get_market = read_url.xpath("//div[@class='infoBox']//@href")
# print(get_market)
for i in get_market:
    get_market1 = "https://www.jkl.com.cn/"+i
    visit_url1 = requests.get(url=get_market1,headers =ua).text
    read_url1 = etree.HTML(visit_url1)
    market_title = read_url1.xpath('//span[@class="con01"]/text()')
    market_place = read_url1.xpath('//span[@class="con02"]/text()')
    market_phone = read_url1.xpath('//span[@class="con03"]/text()')
    market_time = read_url1.xpath('//span[@class="con04"]/text()')
    # print(market_title, market_place,market_phone,market_time)
    get_date = pd.DataFrame({"market_title":market_title
                                ,'market_place':market_place
                                ,'market_phone':market_phone
                                ,'market_time':market_time})
    get_date.to_csv("D:/PYTHONSTUDY/pythonProject7/爬虫/shoplist.csv",index=False,header=0,mode='a',encoding='ANSI')