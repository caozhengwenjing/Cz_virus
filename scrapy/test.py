# 含文件夹（文件夹里的文件）

import xlrd
import requests
import os

print("请输入链接  格式为：C:/Users/Administrator/Desktop/闺蜜时代.xlsx")
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

        name = array['name']
        zheng = array['zheng']
        fan = array['fan']
        hetong = array['hetong'][0:103]
        ide = array['id'][12:15]
        id = ide

        file_name = [name]
        file_name1 = [id]

        path = r'C:\Users\Administrator\Desktop\unt\w'

        for name1 in file_name:
            for id1 in file_name1:
                if not os.path.exists('C:/Users/Administrator/Desktop/unt/%s' % (name1 + id1)):
                    os.mkdir(name1 + id1)

            # print (downloading with requests)

            url = zheng
            url1 = fan
            url2 = hetong

            if url:
                r = requests.get(url)
                with open("C:/Users/Administrator/Desktop/unt/%s/%s.jpg" % (name + id, name), "wb") as code:
                    code.write(r.content)

            elif url1:
                r1 = requests.get(url1)
                with open("C:/Users/Administrator/Desktop/unt/%s/%s.jpg" % (name + id, name + str(1)), "wb") as code:
                    code.write(r1.content)

            else:
                r2 = requests.get(url2)
                with open("C:/Users/Administrator/Desktop/unt/%s/%s.pdf" % (name + id, name), "wb") as code:
                    code.write(r2.content)

            # 反面
            if url1:
                r1 = requests.get(url1)
                with open("C:/Users/Administrator/Desktop/unt/%s/%s.jpg" % (name + id, name + str(1)), "wb") as code:
                    code.write(r1.content)
            else:
                r2 = requests.get(url2)
                with open("C:/Users/Administrator/Desktop/unt/%s/%s.pdf" % (name + id, name), "wb") as code:
                    code.write(r2.content)

            # 合同
            if url2:
                r2 = requests.get(url2)
                with open("C:/Users/Administrator/Desktop/unt/%s/%s.pdf" % (name + id, name), "wb") as code:
                    code.write(r2.content)
            else:
                continue


if __name__ == '__main__':
    # 将excel表格的内容导入到列表中
    import_excel(table)
    for i in tables:
        print(i)
