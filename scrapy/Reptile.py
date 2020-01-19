# 不含文件夹（直接是文件）


import xlrd
import requests
import os
import time

print("请输入链接  格式为：C:/Users/Administrator/Desktop/安徽联云数字科技有限公司.xlsx")
data = input()


# 导入需要读取的第一个Excel表格的路径
data1 = xlrd.open_workbook(data)
table = data1.sheets()[0]
# 创建一个空列表，存储Excel的数据
tables = []


def import_excel(excel):
    for rown in range(excel.nrows):
        array = {'name': '', 'id': '', 'gongsi': '', 'zheng': '', 'fan': '', 'hetong': ''}
        array['name'] = table.cell_value(rown, 0)
        array['id'] = table.cell_value(rown, 1)
        array['gongsi'] = table.cell_value(rown, 2)
        array['zheng'] = table.cell_value(rown, 3)
        array['fan'] = table.cell_value(rown, 4)
        array['hetong'] = table.cell_value(rown, 5)
        tables.append(array)

        # time.sleep(0.25)

        name = array['name']
        zheng = array['zheng']
        fan = array['fan']
        hetong = array['hetong'][0:103]
        id = array['id']

        file_name = [name]
        file_name1 = [id]

        # for name1 in file_name:
        # for id1 in file_name1:
        #     if not os.path.exists('C:/Users/Administrator/Desktop/unt/%s' % (id1)):
        #         os.mkdir(id1)
        #
        url = zheng
        url1 = fan
        url2 = hetong

        if url:
            requests.packages.urllib3.disable_warnings()
            r = requests.get(url, verify=False)
            with open("C:/Users/Administrator/Desktop/unt/%s.jpg" % (name + id + '正'), "wb") as code:
                code.write(r.content)

        elif url1:
            requests.packages.urllib3.disable_warnings()
            r1 = requests.get(url1, verify=False)
            with open("C:/Users/Administrator/Desktop/unt/%s.jpg" % (name + id + '反'), "wb") as code:
                code.write(r1.content)

        else:
            requests.packages.urllib3.disable_warnings()
            r2 = requests.get(url2, verify=False)
            with open("C:/Users/Administrator/Desktop/unt/%s.pdf" % (name + id + '合同'), "wb") as code:
                code.write(r2.content)

        # time.sleep(0.1)

        # 反面
        if url1:
            requests.packages.urllib3.disable_warnings()
            r1 = requests.get(url1, verify=False)
            with open("C:/Users/Administrator/Desktop/unt/%s.jpg" % (name + id + '反'), "wb") as code:
                code.write(r1.content)
        else:
            requests.packages.urllib3.disable_warnings()
            r2 = requests.get(url2, verify=False)
            with open("C:/Users/Administrator/Desktop/unt/%s.pdf" % (name + id + '合同'), "wb") as code:
                code.write(r2.content)

        # time.sleep(0.1)

        # 合同
        if url2:
            requests.packages.urllib3.disable_warnings()
            r2 = requests.get(url2, verify=False)
            with open("C:/Users/Administrator/Desktop/unt/%s.pdf" % (name + id + '合同'), "wb") as code:
                code.write(r2.content)
        else:
            continue
            # time.sleep(0.1)


if __name__ == '__main__':
    # 将excel表格的内容导入到列表中
    import_excel(table)
    for i in tables:
        print(i)
