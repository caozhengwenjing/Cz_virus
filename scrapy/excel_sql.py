import xlrd
import pymysql

# 打开数据所在的工作簿，以及选择存有数据的工作表
book = xlrd.open_workbook("C:/Users/admin/Desktop/三月主播汇总.xlsx")
sheet = book.sheet_by_name("总表")
# 建立一个MySQL连接
conn = pymysql.connect(
    host='192.168.84.196',
    user='root',
    passwd='caozheng',
    db='test',
    port=3306,
    charset='utf8'
)
# 获得游标
cur = conn.cursor()

# 创建插入SQL语句
query = 'insert into zhubo202003_copy2(id,commodity_information,affiliated_shop,sales_volume,payment_amount,unit_sales,\
commission_rate,category_name,clicks,conversion_rate,number_of_clicks,data_time,anchor,week,category)\
 values ( %s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)'
# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
for r in range(1, sheet.nrows):
    id = sheet.cell(r, 14).value
    commodity_information = sheet.cell(r, 0).value
    affiliated_shop = sheet.cell(r, 1).value
    sales_volume = sheet.cell(r, 2).value
    payment_amount = sheet.cell(r, 3).value
    unit_sales = sheet.cell(r, 4).value
    commission_rate = sheet.cell(r, 5).value
    category_name = sheet.cell(r, 6).value
    clicks = sheet.cell(r, 7).value
    conversion_rate = sheet.cell(r, 8).value
    number_of_clicks = sheet.cell(r, 9).value
    data_time1 = sheet.cell(r, 10).value
    print(data_time1)
    # data_time= xldate_as_tuple(data_time1,1).strftime('%Y-%m-%d')
    data_time = xlrd.xldate.xldate_as_datetime(data_time1, 0)
    # data_time = datetime('%Y/%m/%d', localtime(data_time1))
    anchor = sheet.cell(r, 11).value
    week = sheet.cell(r, 12).value
    category = sheet.cell(r, 13).value
    print(data_time)
    values = (id,
              commodity_information,
              affiliated_shop,
              sales_volume,
              payment_amount,
              unit_sales,
              commission_rate,
              category_name,
              clicks,
              conversion_rate,
              number_of_clicks,
              data_time,
              anchor,
              week,
              category)
    # 执行sql语句
    cur.execute(query, values)
cur.close()
conn.commit()
conn.close()
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("导入 " + columns + " 列 " + rows + " 行数据到MySQL数据库!")
