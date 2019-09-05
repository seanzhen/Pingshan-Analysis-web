from pyecharts import Bar, Page, Style, HeatMap,Timeline
from app.charts.constants import WIDTH, HEIGHT
import pandas as pd

def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )

    df = pd.read_csv('./data_cleaned.csv')
    STREET_NAME = df.STREET_NAME.value_counts()
    chart = Bar("街道种类", **style.init_style)
    chart.add("", STREET_NAME.index, STREET_NAME.values,
              mark_point=["max", "min"],
              mark_line=["average"], is_stack=True,
              )
    page.add(chart)

    chart = Timeline(is_auto_play=True, timeline_bottom=0,
                     width=WIDTH, height=HEIGHT)
    for name, c in df.groupby('STREET_NAME'):
        EVENT_TYPE_NAME = c.EVENT_TYPE_NAME.value_counts()
        chart_1 = Bar("各社区事件类型", **style.init_style)
        chart_1.add("", EVENT_TYPE_NAME.index, EVENT_TYPE_NAME.values,
                    mark_point=["max", "min"],
                    mark_line=["average"], is_stack=True)
        chart.add(chart_1, name)
    page.add(chart)

    table = pd.pivot_table(df, index=['STREET_NAME'], columns=['EVENT_TYPE_NAME'], values=['SUB_TYPE_NAME'],
                            aggfunc='count', fill_value=0, margins=1)
    table = table.ix[:-1, :-1]
    comm = list(table.index)
    name = [i[1] for i in table]
    value = [[i, j, float(table.values[i][j])] for i in range(len(comm)) for j in range(len(name))]
    chart = HeatMap("街道与事件热力图", width=WIDTH, height=HEIGHT)
    chart.add("", comm, name, value, is_visualmap=True,
              visual_text_color="#000", visual_orient='horizontal')
    page.add(chart)

    return page
