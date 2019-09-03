from pyecharts import Bar, Page, Style, Timeline, HeatMap, Geo
from app.charts.constants import WIDTH, HEIGHT
import pandas as pd
from collections import defaultdict

def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )

    df = pd.read_csv('C:\\Users\seanz\\Documents\\WORKFILE\\CUHKSZ\\Data Mining\\project\\data_cleaned.csv')

    COMMUNITY_NAME = df.COMMUNITY_NAME.value_counts()
    chart = Bar("社区种类", **style.init_style)
    chart.add("", COMMUNITY_NAME.index, COMMUNITY_NAME.values,
              mark_point=["max", "min"], is_datazoom_show=True,
              mark_line=["average"], is_stack=True,
              datazoom_range=[0, 50])
    page.add(chart)
    coords = {
	'六联社区':[114.332971,22.795219],
	'六和社区':[114.349914,22.707919],
	'南布社区':[114.375607,22.70534],
	'和平社区':[114.355104,22.697106],
	'坑梓社区':[114.390013,22.753031],
	'坪山社区':[114.358844,22.696555],
	'坪环社区':[114.35474,22.688096],
	'江岭社区':[114.362596,22.69202],
	'汤坑社区':[114.331079,22.678805],
	'沙坣社区':[114.377888,22.690889],
	'沙湖社区':[114.326552,22.67909],
	'沙田社区':[114.404444,22.761764],
	'田头社区':[114.410837,22.697197],
	'田心社区':[114.421943,22.700351],
	'石井社区':[114.390978,22.697625],
	'碧岭社区':[114.295663,22.67342],
	'秀新社区':[114.381223,22.746873],
	'竹坑社区':[114.395074,22.715773],
	'老坑社区':[114.369312,22.734866],
	'金沙社区':[114.408079,22.743131],
	'金龟社区':[114.406461,22.663744],
	'马峦社区':[114.359519,22.673022],
	'龙田社区':[114.372841,22.753346]
}
    chart = Geo("坪山区", **style.init_style)
    chart.add("", list(COMMUNITY_NAME.index), list(COMMUNITY_NAME.values), maptype='深圳', type="effectScatter",
              is_random=True, effect_scale=5, is_legend_show=False,
              tooltip_formatter='{b}',visual_range=[0, 4000],
              label_emphasis_textsize=15,is_visualmap=True,
              label_emphasis_pos='right',geo_cities_coords=coords
              )
    page.add(chart)

    chart = Timeline(is_auto_play=True, timeline_bottom=0,
                     width=WIDTH, height=HEIGHT)
    for name, c in df.groupby('COMMUNITY_NAME'):
        EVENT_TYPE_NAME = c.EVENT_TYPE_NAME.value_counts()
        chart_1 = Bar("各社区事件类型", **style.init_style)
        chart_1.add("", EVENT_TYPE_NAME.index, EVENT_TYPE_NAME.values,
                    mark_point=["max", "min"],
                    mark_line=["average"], is_stack=True)
        chart.add(chart_1, name)
    page.add(chart)

    table = pd.pivot_table(df, index=['COMMUNITY_NAME'], columns=['EVENT_TYPE_NAME'], values=['SUB_TYPE_NAME'],
                            aggfunc='count', fill_value=0, margins=1)
    table = table.ix[:-1, :-1]
    comm = list(table.index)
    name = [i[1] for i in table]
    value = [[i, j, float(table.values[i][j])] for i in range(len(comm)) for j in range(len(name))]

    chart = HeatMap("社区与事件热力图", width=WIDTH, height=HEIGHT)
    chart.add("", comm, name, value, is_visualmap=True,
              visual_text_color="#000", visual_orient='horizontal')
    page.add(chart)



    return page
