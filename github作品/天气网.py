# -*- codeing = utf-8 -*-
import requests
from pypinyin import lazy_pinyin
from lxml import etree
cityname = input("请输入城市名称：")
target_list = lazy_pinyin(cityname,style=0)
city_name_all = "".join(target_list)
city_web = f"https://www.tianqi.com/{city_name_all}/"
ua = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
get_website = requests.get(url = city_web,headers = ua).text
get_data = etree.HTML(get_website)
city_name = get_data.xpath("//dd[@class='name']/h1/text()")[0]
city_time = get_data.xpath("//dd[@class='week']/text()")[0]
city_weather = get_data.xpath("//dd[@class='weather']//b/text()")[0]
city_allday_weather = get_data.xpath("//dd[@class='weather']//span/text()")[0]
now_weather = get_data.xpath("//p[@class='now']//b/text()")[0]
other_message = get_data.xpath("//dd[@class='shidu']//b/text()")
other_message = " ".join(other_message)
air_message = get_data.xpath("//dd[@class='kongqi']//h5/text()")[0]
PM =  get_data.xpath("//dd[@class='kongqi']//h6/text()")[0]
PM = PM.split(":")[-1]
PM = PM.strip()
rcl =  get_data.xpath("//dd[@class='kongqi']/span/text()")
rcl = ",".join(rcl)
print(city_name,city_time)
print(f"{city_weather},全天温度{city_allday_weather}，当前温度{now_weather}℃")
print(other_message)
print(rcl)
question = input(f"请问是否要查询{city_name}未来的天气预报?是/否")
if question == "是" or question == 'Y' or question == "y":
    while True:
        day_num = input(f'想查询的天数（输入3/7/10/15/30,输入quit结束程序）')
        if day_num  in ['3','7','10','15','30']:
            future_web = f"https://www.tianqi.com/{city_name_all}/{day_num}/"
            get_website = requests.get(url=future_web, headers=ua).text
            get_data = etree.HTML(get_website)
            city_day1 = get_data.xpath('//span[@class="fl"]/text()')
            city_day2 = get_data.xpath('//span[@class="fr"]/text()')
            city_wea = get_data.xpath('//div[@class="weaul_z"]//text()')

            city_wea = [city_wea[i] + ',' + ''.join(city_wea[i+1:i+5]) for i in range(0,len(city_wea),5) ]
            for i in range(len(city_day1)):
                print(city_day1[i],' ',city_day2[i])
                print(city_wea[i])
        elif day_num == "quit":
                break
        else:
            print("输入错误，请重试！只能查询3/7/10/15/30天,输入quit结束程序")