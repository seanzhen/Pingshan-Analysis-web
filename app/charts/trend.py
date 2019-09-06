from app.charts.constants import WIDTH, HEIGHT
import pandas as pd
from pyecharts import Bar, Page, Style, Pie, Line, HeatMap,Timeline
from collections import defaultdict

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


    month_count = defaultdict(int)
    for month, group in df.groupby('MONTH'):
        month_count[month] = len(group)
    m_s = sorted(list(month_count.keys()))
    m_l = [month_count[i] for i in m_s]
    chart = Line("各月份事件数", **style.init_style)
    chart.add("事件数", m_s, m_l,
              mark_point=["max", "min"],is_more_utils=True,
              mark_line=["average"], is_smooth=True,
              )
    page.add(chart)
    data = df.set_index('CREATE_TIME')
    week_ts = data['COMMUNITY_NAME'].resample('W', how=len)
    week_count = defaultdict(int)
    for i in week_ts.index:
        week_count[i] = week_ts[i]
    w_s = sorted(list(week_count.keys()))
    w_l = [week_count[i] for i in w_s]
    chart = Line("各周事件数", **style.init_style)
    chart.add("事件数", w_s, w_l,
              mark_point=["max", "min"], is_more_utils=True,
              mark_line=["average"], is_smooth=True,
              )
    page.add(chart)


    chart = Timeline(is_auto_play=True, timeline_bottom=0,
                     width=WIDTH, height=HEIGHT)
    for month, group in df.groupby('MONTH'):
        EVENT_TYPE_NAME = group.EVENT_TYPE_NAME.value_counts()
        chart_1 = Bar("问题类型", **style.init_style)
        chart_1.add("", EVENT_TYPE_NAME.index, EVENT_TYPE_NAME.values,
                  mark_point=["max", "min"],
                  mark_line=["average"], is_stack=True)
        chart.add(chart_1,month)
    page.add(chart)

    table = pd.pivot_table(df, index=['MONTH'], columns=['EVENT_TYPE_NAME'], values=['SUB_TYPE_NAME'],
                            aggfunc='count', fill_value=0, margins=1)
    table = table.ix[:-1, :-1]
    comm = list(table.index)
    name = [i[1] for i in table]
    value = [[i, j, float(table.values[i][j])] for i in range(len(comm)) for j in range(len(name))]

    chart = HeatMap("时间与事件热力图", width=WIDTH, height=HEIGHT)
    chart.add("", comm, name, value, is_visualmap=True,
              visual_text_color="#000", visual_orient='horizontal')
    page.add(chart)


    return page
