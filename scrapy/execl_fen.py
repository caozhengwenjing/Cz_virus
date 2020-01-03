import pandas as pd

data = pd.read_excel(r"C:\Users\Administrator\Desktop\杭州河象网络科技有限公司.xlsx")
rows = data.shape[0]  # 获取行数 shape[1]获取列数
department_list = []

for i in range(rows):
    temp = data["服务商"][i]
    if temp not in department_list:
        department_list.append(temp)  # 将服务商的分类存在一个列表中

for department in department_list:
    new_df = pd.DataFrame()

    for i in range(0, rows):
        if data["服务商"][i] == department:
            new_df = pd.concat([new_df, data.iloc[[i], :]], axis=0, ignore_index=True)

    new_df.to_excel(str(department) + ".xlsx", sheet_name=department, index=False)  # 将每个服务商存成一个新excel
