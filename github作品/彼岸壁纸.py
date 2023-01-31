# -*- codeing = utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup


page_n = int(input('请输入爬取的页数:'))
sec_id = int(input('输入图片searchid'))
doc = input(input('请输入所属文件'))

if not os.path.exists(f'D:/PYTHONSTUDY/pythonProject7/实战/壁纸下载/壁纸/{doc}'):
    os.mkdir(f'D:/PYTHONSTUDY/pythonProject7/实战/壁纸下载/壁纸/{doc}')

for page_num in range(0,page_n):
    ua = { "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    wallerpaper_web = f'http://www.netbian.com/e/search/result/index.php?page={page_num}&searchid={sec_id}'

    get_web = requests.get(url = wallerpaper_web,headers = ua).text
    page = BeautifulSoup(get_web,'html.parser')
    image_text = page.find('div', class_='list')
    mic_link = image_text.find_all('a')
    # print(mic_link)
    all_link =[]
    for i in mic_link:
        pic = 'http://www.netbian.com/' + i['href']
        all_link.append(pic)
    for i in all_link:
        get_pic = requests.get(url=i, headers=ua)
        get_pic.encoding = "gbk"
        get_url = BeautifulSoup(get_pic.text,'html.parser')
        pic_link = get_url.find('div',class_="pic")
        pic_link = pic_link.find_all('img')
        # print(pic_link)

        for x in pic_link:
            pic_name = x['alt']
            pic_link = x['src']
            print(pic_name + '下载成功')
            pic_link_down = requests.get(url = pic_link).content

            down_load = f'D:/PYTHONSTUDY/pythonProject7/实战/壁纸下载/壁纸/{doc}/' + pic_name +'.' +'png'
            with open(down_load,'wb') as y:
                y.write(pic_link_down)
