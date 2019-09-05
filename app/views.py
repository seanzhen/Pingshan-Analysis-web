from flask import render_template
import app.charts as charts

from . import app


@app.route("/")
def hello():
    return render_template('index.html',
                           title='首页')


@app.route('/event_type')
def event_type():
    _event_type= charts.event_type.create_charts()
    return render_template('base.html',
                           title='事件类型',
                           source_file='event_type',
                           myechart=_event_type.render_embed(),
                           script_list=_event_type.get_js_dependencies())


@app.route('/comm')
def comm():
    _comm = charts.comm.create_charts()
    return render_template('base.html',
                           title='社区街道与事件',
                           source_file='comm',
                           myechart=_comm.render_embed(),
                           script_list=_comm.get_js_dependencies())

@app.route('/street')
def street():
    _street = charts.street.create_charts()
    return render_template('base.html',
                           title='街道与事件',
                           source_file='street',
                           myechart=_street.render_embed(),
                           script_list=_street.get_js_dependencies())


@app.route('/src_event')
def src_event():
    _src_event = charts.src_event.create_charts()
    return render_template('base.html',
                           title='投诉渠道与事件',
                           source_file='src_event',
                           myechart=_src_event.render_embed(),
                           script_list=_src_event.get_js_dependencies())


@app.route('/cluster')
def cluster():
    _cluster = charts.cluster.create_charts()
    return render_template('base.html',
                           title='社区聚类分析',
                           source_file='cluster',
                           myechart=_cluster.render_embed(),
                           script_list=_cluster.get_js_dependencies())


@app.route('/over')
def over():
    _over = charts.over.create_charts()
    return render_template('base.html',
                           title='超时预测',
                           source_file='over_time',
                           myechart=_over.render_embed(),
                           script_list=_over.get_js_dependencies())


@app.route('/rule')
def rule():
    _rule = charts.rule.create_charts()
    return render_template('base.html',
                           title='事件关联规则分析',
                           source_file='rule',
                           myechart=_rule.render_embed(),
                           script_list=_rule.get_js_dependencies())



@app.route('/trend')
def trend():
    _trend = charts.trend.create_charts()
    return render_template('base.html',
                           title='事件趋势',
                           source_file='trend',
                           myechart=_trend.render_embed(),
                           script_list=_trend.get_js_dependencies())


@app.route('/rec_event')
def rec_event():
    _rec_event = charts.rec_event.create_charts()
    return render_template('base.html',
                           title='处理部门与事件',
                           source_file='rec_event',
                           myechart=_rec_event.render_embed(),
                           script_list=_rec_event.get_js_dependencies())



@app.route('/comm_trend')
def comm_trend():
    _comm_trend = charts.comm_trend.create_charts()
    return render_template('base.html',
                           title='社区与事件',
                           source_file='scatter',
                           myechart=_comm_trend.render_embed(),
                           script_list=_comm_trend.get_js_dependencies())


@app.route('/street_trend')
def street_trend():
    _street_trend = charts.street_trend.create_charts()
    return render_template('base.html',
                           title='街道与事件',
                           source_file='street_trend',
                           myechart=_street_trend.render_embed(),
                           script_list=_street_trend.get_js_dependencies())







@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route("/conclusion")
def conclusion():
    return render_template('conclusion.html',
                           title='总结')

@app.route("/overtime")
def overtime():
    return render_template('overtime.html',
                           title='超时预测')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html',
                           title='dashboard')