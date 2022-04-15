# 导入模块
import pyecharts.options as opts
from pyecharts.charts import Pie
from pyecharts.charts import Gauge
import pandas as pd

df = pd.read_excel('myLife.xlsx', sheet_name='Scene')
# 读取myLife中Scene这个表格
df = df.groupby(df['天气'], as_index=False).count()
# 对天气进行分组并统计次数
df = df['日期']
# 只取日期这一行
print(df)

x_data = ["多云", "阴", "晴", "小雨"]
# 饼图的变量
y_data = df
data_pair = [list(z) for z in zip(x_data, y_data)]
# 导入这个数据为xyz值
data_pair.sort(key=lambda x: x[1])
# 元素x:x[]字母可以随意修改，
# 求最大值方式按照中括号[]里面的维度，
# [0]按照第一维，[1]按照第二维。
(
    Pie(init_opts=opts.InitOpts(height="500px", bg_color="#2c343c"))
        #  height="500px" 屏幕分辨率 500 bg_color="#2c343c"设置颜色

        .add(
        series_name="晴",
        # 饼图的变量命名
        data_pair=data_pair,
        # 访问来源
        rosetype="radius",
        # 扇区圆心角展现数据的百分比
        radius="55%",
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
        # is_show=False 设置颜色 position 定位机制 center 描述当前界面元素的中心点在其父界面元素中的位置
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title="天气占比图",
            # 这是饼图的名字
            pos_left="center",
            pos_top="20",
            # 字体大小
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
            # 颜色
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
        .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
        .render("天气占比图.html")
)
