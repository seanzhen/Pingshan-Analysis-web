from pyecharts import Bar, HeatMap,Timeline, Page, Style,Line
from app.charts.constants import HEIGHT, WIDTH
import pandas as pd
from collections import defaultdict



def create_charts():
    page = Page()
    style = Style(
        width=WIDTH, height=HEIGHT
    )
    df = pd.read_csv('C:\\Users\seanz\\Documents\\WORKFILE\\CUHKSZ\\Data Mining\\project\\data_cleaned.csv')
    table6 = pd.pivot_table(df, values=['DISPOSE_UNIT_NAME'], index=['INTIME_ARCHIVE_NUM'],
                            columns=['EVENT_TYPE_NAME'], aggfunc='count', fill_value=0)
    table6_2 = table6 / table6.sum()
    name = [i[1] for i in table6_2]
    value = [float(table6_2.values[0][j]) for j in range(len(name))]
    chart = Bar("超时结案", **style.init_style)
    chart.add("", name, value,
              is_datazoom_show=True,
              mark_line=["average"],is_stack=True,
              datazoom_type='both',datazoom_range=[10, 60])
    page.add(chart)

    return page
