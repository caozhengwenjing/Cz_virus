import requests
import json
import tablib

print("请输入直播明细连接")
url_ming = input()
# ur2 = "https://apimwcs.mogujie.com/h5/mwp.livelist.adcRoomItemInfo/1/?data=%7B%22pageNum%22%3A1%2C%22pageSize%22%3A10%2C%22itemName%22%3A%22%22%2C%22itemUrl%22%3A%22%22%2C%22roomId%22%3A%221dy12m%22%7D&mw-appkey=100028&mw-ttid=NMMain%40mgj_pc_1.0&mw-t=1587018686468&mw-uuid=8c183fb2-7051-486e-be77-3eacbdf2c1d5&mw-h5-os=unknown&mw-sign=eba4c2b0f62006d6da4b80fa69a996dc&callback=mwpCb2&_=1587018686470"
ur2 = url_ming

# 字典，key是固定的
h = {
    'Host': 'apimwcs.mogujie.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Sec-Fetch-Dest': 'script',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Referer': 'https://pc.mogujie.com/assistant/index.html?ptp=31.HS8WT.0.0.S9YEIvxZ',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '__mgjuuid=8c183fb2-7051-486e-be77-3eacbdf2c1d5; _mwp_h5_token_enc=8be096ee6cf137a63667b2271e0d6aef; _mwp_h5_token=a688099ffd23af8d8861aada0a451c26_1586507735361; FRMS_FINGERPRINTN=HTvZZvVLQ7GkFuoBgKjjxw; __mogujie=HbEX41eorQIZs308rUvjU33EUtHdBTgqmVtAavjLXYhsQyBajTTJrJry7XsqzJol5A0XRs0jsgg4aaGyHgANKA%3D%3D; __ud_=1eoe7vc; __must_from=10000000_; _ga=GA1.2.250068851.1587009101; _gid=GA1.2.1963589664.1587009101'
}

# 设置代理
proxies = {
    "http": "118.112.195.152",
    # "http": "118.212.107.105",
    # "http": "183.166.96.2",
    # "http": "182.87.45.2",
    # "http": "60.13.42.140",
    # "http": "182.34.36.194",
    # "http": "182.138.238.150",
    # "http": "182.46.110.222",
    # "http": "27.43.191.84",
    # "http": "183.230.179.164",
    # "http": "60.205.132.71",
    # "http": "171.35.167.173",
    # "http": "58.253.154.8",
}
requests.packages.urllib3.disable_warnings()

# 下部分数据表格
response1 = requests.get(ur2, headers=h, proxies=proxies, verify=False)
text1 = response1.text
# 得到数据
print(text1)
# 去除没用字符
print('请输入删除的字符')
de = input()

input()
ioa1 = str(text1).strip("'%s'" % de).strip(')')
print(ioa1)
jsonobj1 = json.loads(ioa1, strict=False)  # 将响应内容转换为Json对象
toCntPercent1 = jsonobj1['data']['list']  # 从Json对象获取想要的内容
print(toCntPercent1)

# 商品列表数据导入
# 将json中的key作为header, 也可以自定义header（列名）——商品列表
header1 = tuple([i for i in toCntPercent1[0].keys()])

data1 = []
# 循环里面的字典，将value作为数据写入进去
for row1 in toCntPercent1:
    body = []
    for v in row1.values():
        body.append(v)
    data1.append(tuple(body))

data1 = tablib.Dataset(*data1, headers=header1)
print(data1)

print("请输入保存的文件名")
wen = input()
open('%s.xls' % wen, 'wb').write(data1.xls)
