# -*- codeing = utf-8 -*-
import requests
from lxml import etree
import  pandas as pd

wb_web = 'https://xm.58.com/ershoufang/?PGTID=0d100000-0025-ed6b-704e-99201c7d55c3&ClickID=2'
ua = { "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

get_web = requests.get(url = wb_web, headers = ua).text
get_data = etree.HTML(get_web)

house_title = get_data.xpath('//div[@class="property-content-title"]/h3/text()')
# print(house_title)
house_price = get_data.xpath('//p[@class="property-price-total"]//text()')
house_price = [''.join(house_price[i:i+3]) for i in range(0,len(house_price),3)]
# print(house_price)

download_target = f'D:/PYTHONSTUDY/pythonProject7/实战/58二手房/58esf.xlsx'
download = pd.DataFrame({"名称":house_title,"价格":house_price})
download.index = download.index + 1
download.to_excel(download_target)