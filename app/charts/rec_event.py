from pyecharts import Bar, HeatMap,Timeline, Page, Style,Line
from app.charts.constants import HEIGHT, WIDTH
import pandas as pd
from collections import defaultdict
import re
def deletekh(s):
    a = re.sub(u"\\（.*?\\）", "", s)
    return a


def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )
    df = pd.read_csv('./data_cleaned.csv')
    df['CREATE_TIME'] = pd.to_datetime(df['CREATE_TIME'])
    df['MONTH'] = 0
    months = []
    for i in df.CREATE_TIME:
        month = i.strftime("%Y-%m")
        months.append(month)
    df.MONTH = months
    df['DISPOSE_UNIT_NAME_DIST'] = 0
    df['DISPOSE_UNIT_NAME_DIST'] = df['DISPOSE_UNIT_NAME'].apply(deletekh)

    DISPOSE_UNIT_NAME_DIST = df.DISPOSE_UNIT_NAME_DIST.value_counts()
    chart = Bar("处理部门", **style.init_style)
    chart.add("", DISPOSE_UNIT_NAME_DIST.index, DISPOSE_UNIT_NAME_DIST.values,
              mark_point=["max", "min"],is_datazoom_show=True,datazoom_range=[0,30],
              mark_line=["average"], is_stack=True)
    page.add(chart)

    chart = Timeline(is_auto_play=True, timeline_bottom=0,
                     width=WIDTH, height=HEIGHT)
    for month, group in df.groupby('MONTH'):
        DISPOSE_UNIT_NAME = group.DISPOSE_UNIT_NAME_DIST.value_counts()
        chart_1 = Bar("处理部门事件数", **style.init_style)
        chart_1.add("", DISPOSE_UNIT_NAME.index, DISPOSE_UNIT_NAME.values,
                  mark_point=["max", "min"],
                  mark_line=["average"], is_stack=True)
        chart.add(chart_1,month)
    page.add(chart)


    return page
