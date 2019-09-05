from pyecharts import Graph, Page, Style
import pandas as pd

def create_charts():
    page = Page()

    style = Style(
        width=1100, height=600
    )

    df = pd.read_csv(
        './处置部门关联规则.csv')

    x_list = list(df['lhs'].values)
    y_list = list(df['rhs'].values)
    sup = list(df['sup_lhs'])
    conf = list(df['conf'])
    nodes = []
    links = []
    all_list = []
    all_list.extend(x_list)
    all_list.extend(y_list)
    all_list = list(set(all_list))
    for i in range(len(all_list)):
        nodes.append({"name": all_list[i],
                      "symbolSize": 10,
                      "label": {"normal": {"show": "True"}
                      }})

    for j in range(len(x_list)):
        links.append({"source": x_list[j], "target": y_list[j]})

    # print(nodes)
    # print(links)
    chart = Graph("关联规则", **style.init_style)
    chart.add("", nodes, links,  label_pos="right", graph_repulsion=1000,
              is_legend_show=False, line_curve=0.2, label_text_color=None)
    page.add(chart)


    comm_name = ['竹坑社区','沙田社区','龙田社区','秀新社区','金沙社区',
                 '碧岭社区','老坑社区','和平社区','六和社区','六联社区',
                 '坪山社区']
    nodes = []
    links = []
    categories = []
    for name in comm_name:
        # print(name)
        df = pd.read_csv(
            './'+name+'.csv')
        x_list = list(df['lhs'].values)
        y_list = list(df['rhs'].values)
        all_list = []
        all_list.extend(x_list)
        all_list.extend(y_list)
        all_list = list(set(all_list))
        for i in range(len(all_list)):
            # print(all_list[i])
            nodes.append({"name": name+all_list[i],
                          "symbolSize": 10,
                          "draggable": "False",
                          "category": name,
                          "label": {"normal": {"show": "True"}
                          }})
        categories.append({"name": name})

        for j in range(len(x_list)):
            links.append({"source": name+x_list[j], "target": name+y_list[j]})

    chart = Graph("", **style.init_style)
    chart.add("", nodes, links, categories, label_pos="right", graph_repulsion=1000,
              is_legend_show=True, line_curve=0.2, label_text_color=None)
    page.add(chart)

    return page
