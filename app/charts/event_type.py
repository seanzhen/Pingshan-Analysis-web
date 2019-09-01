import random
import pandas as pd
from pyecharts import Bar, Page, Style, Pie, WordCloud
from app.charts.constants import WIDTH, HEIGHT

import re
import datetime
df = pd.read_csv('C:\\Users\seanz\\Documents\\WORKFILE\\CUHKSZ\\Data Mining\\project\\data_cleaned.csv')

def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )
    a = df.EVENT_PROPERTY_NAME.value_counts() / len(df.EVENT_PROPERTY_NAME)
    chart = Pie("事件类型占比", title_pos='center', **style.init_style)
    chart.add("", a.index, a.values, label_text_color=None, is_random=True,
              is_label_show=True, legend_pos='left')
    page.add(chart)

    EVENT_TYPE_NAME = df.EVENT_TYPE_NAME.value_counts()
    chart = Bar("问题类型", **style.init_style)
    chart.add("", EVENT_TYPE_NAME.index, EVENT_TYPE_NAME.values,
              mark_point=["max", "min"],is_datazoom_show=True,
              mark_line=["average"],is_stack=True,
              datazoom_type='both',datazoom_range=[10, 60])
    page.add(chart)

    MAIN_TYPE_NAME = df.MAIN_TYPE_NAME.value_counts()
    chart = WordCloud("大类名称", **style.init_style)
    chart.add("", MAIN_TYPE_NAME.index, MAIN_TYPE_NAME.values
              , word_size_range=[30, 100], rotate_step=66)
    page.add(chart)

    chart = Bar("问题类型", **style.init_style)
    chart.add("", MAIN_TYPE_NAME.index, MAIN_TYPE_NAME.values,
              mark_point=["max", "min"], is_datazoom_show=True,
              mark_line=["average"], is_stack=True,
              datazoom_type='both', datazoom_range=[10, 60])
    page.add(chart)

    SUB_TYPE_NAME = df.SUB_TYPE_NAME.value_counts()
    chart = WordCloud("小类名称", **style.init_style)
    chart.add("", SUB_TYPE_NAME.index, SUB_TYPE_NAME.values
              , word_size_range=[30, 100], rotate_step=66)
    page.add(chart)

    chart = Bar("问题类型", **style.init_style)
    chart.add("", SUB_TYPE_NAME.index, SUB_TYPE_NAME.values,
              mark_point=["max", "min"], is_datazoom_show=True,
              mark_line=["average"], is_stack=True,
              datazoom_type='both', datazoom_range=[10, 60])
    page.add(chart)



    return page
