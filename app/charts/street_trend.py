from pyecharts import Scatter, Page, Style, Line, Timeline, Bar
from app.charts.constants import WIDTH, HEIGHT
import pandas as pd
from collections import defaultdict


def create_charts():
    page = Page()
    style = Style(
        width=WIDTH, height=HEIGHT
    )
    df = pd.read_csv('C:\\Users\seanz\\Documents\\WORKFILE\\CUHKSZ\\Data Mining\\project\\data_cleaned.csv')

    df['CREATE_TIME'] = pd.to_datetime(df['CREATE_TIME'])

    df['MONTH'] = 0

    months = []
    for i in df.CREATE_TIME:
        month = i.strftime("%Y-%m")
        months.append(month)
    df.MONTH = months

    chart = Timeline(is_auto_play=True, timeline_bottom=0,
                     width=WIDTH, height=HEIGHT)
    for name, c in df.groupby('STREET_NAME'):
        month_count = defaultdict(int)
        for month, group in c.groupby('MONTH'):
            month_count[month] = len(group)

        chart_1 = Line("各月份事件数", **style.init_style)
        chart_1.add("事件数", list(month_count.keys()), list(month_count.values()),
                  mark_point=["max", "min"],is_more_utils=True,
                  mark_line=["average"], is_smooth=True,
                  )
        chart.add(chart_1,name)
    page.add(chart)

    chart = Timeline(is_auto_play=True, timeline_bottom=0,
                     width=WIDTH, height=HEIGHT)
    for month, group in df.groupby('MONTH'):
        STREET_NAME = group.STREET_NAME.value_counts()
        chart_1 = Bar("", **style.init_style)
        chart_1.add("", STREET_NAME.index, STREET_NAME.values,
                  mark_point=["max", "min"],
                  mark_line=["average"], is_stack=True)
        chart.add(chart_1,month)
    page.add(chart)


    return page
