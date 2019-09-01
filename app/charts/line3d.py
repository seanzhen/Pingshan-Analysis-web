import math
import pandas as pd
from pyecharts import Line3D, Page, Style,Scatter3D
from app.charts.constants import RANGE_COLOR, WIDTH, HEIGHT


def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )
    df = pd.read_csv(
        'C:\\Users\seanz\\Documents\\WORKFILE\\CUHKSZ\\Data Mining\\project\\处置部门关联规则.csv')

    x_list = list(df['lhs'].values)
    y_list = list(df['rhs'].values)
    value = list(df['conf'])
    data = [
        [x_list[i],
         y_list[i],
         float(value[i])] for i in range(len(x_list))
    ]
    chart = Scatter3D("PCA & K-means", **style.init_style)
    chart.add('', data, is_visualmap=True, visual_range_color=RANGE_COLOR)
    page.add(chart)

    return page
