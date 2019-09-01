from pyecharts import EffectScatter, Page, Style,Scatter,TreeMap
from app.charts.constants import WIDTH, HEIGHT
import pandas as pd

def create_charts():
    page = Page()

    style = Style(
        width=WIDTH, height=HEIGHT
    )

    df = pd.read_csv('./Cluster_Result_Visualization.csv')
    chart = Scatter("PCA & K-means", **style.init_style)
    for name, group in df.groupby('Class'):
        if name == 0:
            sym = 'pin'
        elif name== 1:
            sym = 'triangle'
        else:
            sym = 'rect'
        x_l = []
        y_l = []
        c_l = []
        for i in range(len(group)):
            x_l.append(round(float(group.iloc[i]['X']),2))
            y_l.append(round(float(group.iloc[i]['Y']),2))
            c_l.append(group.iloc[i]['COMMUNITY_NAME'])

        chart.add(str(name),x_l, y_l,extra_name=c_l,
                  symbol_size=20, effect_scale=3.5,
                  effect_period=3, symbol=sym)
    page.add(chart)

    data = [
        {
            "value": 23,
            "name": "市政设置",
            "children": [
                {
                    "value": 20,
                    "name": "组织人事",
                    "children": [
                        {
                            "value": 2,
                            "name": "group A",
                        },
                        {
                            "value": 18,
                            "name": "group B",
                        }]
                },
                {
                    "value": 3,
                    "name": "group C",
                }]}
    ]

    chart = TreeMap("Decision Tree", width=WIDTH, height=HEIGHT)
    chart.add("事件", data, is_label_show=True, label_pos='inside',treemap_left_depth=1)
    page.add(chart)

    return page
