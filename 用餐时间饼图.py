import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False  # 解决中文显示问题
# 获取数据
v = []
df = pd.read_excel('myLife.xlsx', sheet_name='Activity')
df = df.loc[df["操作"] == "吃早餐"]
df1 = df['时长'].sum()
a = round(df1)  # 对浮点数进行四舍五入取整数
v.insert(0, a)  # 让数据插入列表
df = pd.read_excel('myLife.xlsx', sheet_name='Activity')
df = df.loc[df["操作"] == "吃午餐"]
df2 = df['时长'].sum()
b = round(df2)
v.insert(1, b)
df = pd.read_excel('myLife.xlsx', sheet_name='Activity')
df = df.loc[df["操作"] == "吃晚餐"]
df3 = df['时长'].sum()
c = round(df3)
v.insert(2, c)
n = a + b + c  # 总数据
labels = ['吃早餐', '吃午餐', '吃晚餐']  # 数据标签
colors = ['red', 'green', 'yellow']  # 各区域颜色
sizes = [v[0] / n * 100, v[1] / n * 100, v[2] / n * 100]  # 数据计算处理
expodes = (0, 0, 0)  # 设置突出模块偏移值
plt.title('用餐时间占比')  # 加标题
plt.pie(sizes, labels=labels, explode=expodes, shadow=True, colors=colors, autopct='%2.2f%%')
# 设置绘图属性并绘图,autopct--显示3位整数一位小数
plt.axis('equal')  # 用于显示为一个长宽相等的饼图
plt.savefig('aaa')  # 保存并显示
plt.show()
