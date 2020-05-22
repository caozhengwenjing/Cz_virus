import os
import requests
import json
import pandas as pd
import urllib.request
import random


def parse_page(url):
    cookie = input('请输入cookie：')

    # 解析url时所需要带的请求头
    headers = {
        'Host': 'taobaolive.taobao.com',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'Sec-Fetch-Dest': 'empty',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://taobaolive.taobao.com/room/index.htm?spm=a21bo.2017.523825.1.5af911d9INwxkI&feedId=263308000218',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': cookie
    }

    # 设置代理
    proxy = [
        {
            'http': 'http://14.20.235.54',
            'https': 'http://14.20.235.54',
        },
        {
            'http': 'http://118.114.77.47:8080',
            'https': 'http://118.114.77.47:8080',
        },
        {
            'http': 'http://112.114.31.177:808',
            'https': 'http://112.114.31.177:808',
        },
        {
            'http': 'http://183.159.92.117:18118',
            'https': 'http://183.159.92.117:18118',
        },
        {
            'http': 'http://110.73.10.186:8123',
            'https': 'http://110.73.10.186:8123',
        },
    ]

    response = requests.get(url, headers=headers, proxies=random.choice(proxy), verify=False)
    text = response.text
    print(text)
    state = json.loads(response.content)

    with open("feiyan.json", "w", encoding='utf-8') as f:
        f.write(json.dumps(state, indent=2, ensure_ascii=False))
        print("保存成功")
    jsonobj = json.loads(text, strict=False)  # 将响应内容转换为Json对象
    provincelen = len(jsonobj['result']['data']['itemList'])

    i = 0
    list_name = []
    list_pic = []
    # list_category = []
    anchor = input('请输入主播名：')
    if not os.path.exists('E:\图片\%s' % (anchor)):
        os.mkdir(anchor)
    for i in range(provincelen):
        if state['result']['data']['itemList'][i]['goodsIndex'] is None:
            continue
        name = state['result']['data']['itemList'][i]['goodsList'][0]['itemName']
        pic = state['result']['data']['itemList'][i]['goodsList'][0]['itemPic']
        shopping_url = state['result']['data']['itemList'][i]['goodsList'][0]['itemH5TaokeUrl']
        # category = state['result']['data']['itemList'][i]['goodsList']['extendVal'][0]['categoryLevelOneName']
        list_name.append(name)
        list_pic.append(shopping_url)
        # list_category.append(category)

        pict = str('http:') + pic
        path = f"E:\图片\%s\{i}.jpg" % anchor
        urllib.request.urlretrieve(pict, path)

    data = {
        "商品名称": list_name,
        "商品链接": list_pic,
        # "商品类目": list_category
    }
    df_excel = pd.DataFrame(data)
    file = input('请输入文件名：')
    df_excel.to_excel(rf'C:\Users\admin\Desktop\{file}.xls')


def main():
    url = input('请输入链接：')
    parse_page(url)

if __name__ == '__main__':
    main()
