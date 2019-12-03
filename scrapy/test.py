import xlrd
import requests
import os

# 导入需要读取的第一个Excel表格的路径
data1 = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\掌小门1\安徽人联计算机科技有限公司.xlsx")
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
        hetong = array['hetong']
        id = array['id']

        file_name = [name]
        # path = r'C:\Users\Administrator\Desktop\test\w'

        #循环判断文件夹是否存在，不存在则自动创建
        for name1 in file_name:
            if not os.path.exists('C:/Users/Administrator/Desktop/test/%s' % (name1)):
                os.mkdir(name1)

        # print (downloading with requests)

        url = zheng
        url1 = fan
        url2 = hetong
        # 获取姓名
        r = requests.get(url)
        with open("C:/Users/Administrator/Desktop/test/%s/%s.jpg" % (name,name), "wb") as code:
            code.write(r.content)
        # 获取正面
        r1 = requests.get(url1)
        with open("C:/Users/Administrator/Desktop/test/%s/%s.jpg" % (name,name+str(1)), "wb") as code:
            code.write(r1.content)
        # 获取反面
        r2 = requests.get(url2)
        with open("C:/Users/Administrator/Desktop/test/%s/%s.pdf" % (name,name), "wb") as code:
            code.write(r2.content)



if __name__ == '__main__':
    # 将excel表格的内容导入到列表中
    import_excel(table)
    for i in tables:
        print(i)


