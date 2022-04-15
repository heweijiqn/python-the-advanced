import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd
import numpy as np

# 导入需要的模块

df_act = pd.read_excel('myLife.xlsx', sheet_name='Scene')
# 获取Scene表所有数据
lastRow = df_act.shape[0]
# 规定Scene表的最后一行

x_data = ['{}日'.format(i) for i in range(1, 32)]
# 循环日期，确定x轴

month_name_list = x_data

df = df_act[['最低温度']]
df = np.array(df)
# 将df转化为数组
df = df.tolist()
# 将df转化为list，将二维数组转化为列表

df1 = df
df1 = df1[30:]
# 切片，从日期那一行开始取，取到第30行

df = df_act[['最高温度']]
df = np.array(df)
df = df.tolist()

df2 = df
df2 = df2[30:]

low_temperature = df1

high_temperature = df2

(
    Line(init_opts=opts.InitOpts(width="1000px", height="600px"))
        # 设置图表中的x轴和y轴长度
        .add_xaxis(xaxis_data=month_name_list)
        # 导入x轴的数据
        .add_yaxis(
        series_name="最高气温",
        y_axis=high_temperature,
        # 导入y轴最高气温数据
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                # 对最高气温的最高值进行标记
                opts.MarkPointItem(type_="min", name="最小值"),
                # 对最高气温的最低值进行标记
            ]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
            # 取最高气温的平均值
        ),
    )
        .add_yaxis(
        series_name="最低气温",
        # 导入y轴最低气温数据
        y_axis=low_temperature,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(value=-2, name="周最低", x=1, y=-1.5)]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average", name="平均值"),
                # 取最低气温的平均值
                opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
                # 对最低气温的最高值进行标记
                opts.MarkPointItem(type_="min", name="最小值"),
                # 对最低气温的最低值进行标记
                opts.MarkLineItem(symbol="none", x="90%", y="max"),
            ]
        ),
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="12月气温变化"),
        # 标明图表的名字
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        # trigger为触发器
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        # category 是 pandas 的一种数据类型，对应着被统计的变量
        # boundary_gap=False为贴边没有边距
    )
        .render("temperature_change_line_chart.html")
    # 生成图表"temperature_change_line_chart.html"
)
