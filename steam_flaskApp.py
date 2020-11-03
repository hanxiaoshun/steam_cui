# from flask.ext.login import login_required, login_user, logout_user
from flask import Flask, url_for, request, redirect, render_template, make_response, send_file, session
from flask import request
from code.task_thread import *
import json
import time
import os
from werkzeug.utils import secure_filename
# from code.mongoAuth import MainMongodb
import json
import logging.config
import os
import queue
from code.controller import Controller
import random
import logging
from code.utils import *

#
# host = '127.0.0.1'
# port = 27017
# mongo = MainMongodb(host=host, port=port)
# sms_tracking = 'sms_tracking'
# registry_tracking = 'registry_tracking'
# code_tracking = 'code_tracking'
"""
首页
"""
date_time_str = str(time.strftime(
    '%Y-%m-%d_%H-%M-%S', time.localtime(time.time())))
app = Flask(__name__)

app.secret_key = "qsgtdkoaslak,,lkfgf8od032-2856ldjkgd"


class TaskNumber(object):
    def __init__(self):
        self.origin_detail_len = 0


task_number = TaskNumber()


def setup_logging(default_path="logging.json", default_level=logging.INFO, env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            config = json.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('username')
        pwd = request.form.get('password')
        if user == 'cui' and pwd == '123456':
            session['username'] = user
            return redirect('/')
        else:
            return render_template('login.html', msg='用户或密码错误')


@app.route('/login_out', methods=['GET', 'POST'])
def login_out():
    if not session.get('username'):
        session.pop('username')  # 删除session
    return redirect('/')


# @app.route('/', methods=['GET'])
# def signin_form():
#     return '''
#               <hr>
#                 <a href="/start" target=“_blank”>start</a>
#               <hr>
#               '''

"""
访问路径
"""


def login_required(func):
    def inner(*args, **kwargs):
        if not session.get('username'):
            return redirect('/login')
        return func(*args, **kwargs)

    return inner


@app.route('/', methods=['GET'], endpoint='/')
@login_required
def signin_form(name=None):
    return render_template('index.html', name=name)


@app.route('/patch_time', methods=['POST'], endpoint='patch_time')
@login_required
def patch_time():
    return date_time_str


@app.route('/setting_prefix', methods=['POST'], endpoint='setting_prefix')
@login_required
def setting_prefix():
    """
    设置前缀，储存在文件中
    :return:
    """
    prefix = request.form['setting_prefix']
    with open('setting_prefix.txt', 'w', encoding='utf-8') as setting_prefix_f:
        setting_prefix_f.write(prefix)
    return 'ok'


@app.route('/setting_prefix_check', methods=['POST'], endpoint='setting_prefix_check')
@login_required
def setting_prefix_check():
    """
    设置前缀，储存在文件中
    :return:
    """
    if os.path.exists('setting_prefix.txt'):
        with open('setting_prefix.txt', 'r', encoding='utf-8') as setting_prefix_f:
            return setting_prefix_f.read()
    else:
        return 'no'


@app.route('/upload_email_list_file', methods=['POST'], endpoint='upload_email_list_file')
@login_required
def upload_email_list_file():
    """
    导入邮箱列表
    :return:
    """
    if request.method == 'POST':
        f = request.files['email_list_file']
        # filename = f.filename
        if os.path.exists("email_list_file.txt"):
            os.remove("email_list_file.txt")
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, secure_filename("email_list_file.txt"))
        f.save(upload_path)

    if os.path.exists("email_list_file_already_use.txt"):
        with open("email_list_file_already_use.txt", 'r+', encoding='utf-8') as email_list_file_already_use_f:
            email_list_file_already_use_f.truncate()
    else:
        with open("email_list_file_already_use.txt", 'w', encoding='utf-8') as email_list_file_already_use_f:
            email_list_file_already_use_f.write("")
        # return redirect(url_for('upload_proxy_listfile'))
    return "文件上传成功，已替换原始 邮箱列表文件。。。<a href='/'>返回首页</a>"


@app.route('/email_can_use', methods=['POST'], endpoint='email_can_use')
@login_required
def email_can_use():
    result = {'can_use': 0, 'already_use': 0}
    if os.path.exists("email_list_file.txt"):
        with open("email_list_file.txt", 'r', encoding='utf-8') as email_list_file_f:
            can_use = len(email_list_file_f.readlines())
        # 待执行的人物列表
        task_number.origin_detail_len = can_use
        if os.path.exists("email_list_file_already_use.txt"):
            with open("email_list_file_already_use.txt", 'r', encoding='utf-8') as email_list_file_already_use_f:
                already_use = len(email_list_file_already_use_f.readlines())
        result['can_use'] = can_use
        result['already_use'] = already_use
    else:
        pass
    return json.dumps(result, ensure_ascii=False)


@app.route('/upload_ip_list', methods=['POST'], endpoint='upload_ip_list')
@login_required
def upload_ip_list():
    """
    导入邮箱列表
    :return:
    """
    if request.method == 'POST':
        f = request.files['file_ip_list']
        # filename = f.filename
        if os.path.exists("file_ip_list.txt"):
            os.remove("file_ip_list.txt")
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, secure_filename("file_ip_list.txt"))
        f.save(upload_path)

    if os.path.exists("file_ip_list_already_use.txt"):
        with open("file_ip_list_already_use.txt", 'r+', encoding='utf-8') as file_ip_list_already_use_f:
            file_ip_list_already_use_f.truncate()
    else:
        with open("file_ip_list_already_use.txt", 'w', encoding='utf-8') as file_ip_list_already_use_f:
            file_ip_list_already_use_f.write("")
        # return redirect(url_for('upload_proxy_listfile'))
    return "文件上传成功，已替换原始 IP列表文件。。。<a href='/'>返回首页</a>"


@app.route('/ip_can_use', methods=['POST'], endpoint='ip_can_use')
@login_required
def ip_can_use():
    result = {'can_use': 0, 'already_use': 0}
    if os.path.exists("file_ip_list.txt"):
        with open("file_ip_list.txt", 'r', encoding='utf-8') as file_ip_list_f:
            can_use = len(file_ip_list_f.readlines())
        if os.path.exists("file_ip_list_already_use.txt"):
            with open("file_ip_list_already_use.txt", 'r', encoding='utf-8') as file_ip_list_already_use_f:
                already_use = len(file_ip_list_already_use_f.readlines())
        result['can_use'] = can_use
        result['already_use'] = already_use
    else:
        pass

    return json.dumps(result, ensure_ascii=False)


def start_registry(start=1, count=None):
    """
    跳转controller
    :param start:
    :param count:
    :return:
    """

    start_thread_queue(date_time_str)


@app.route('/registry', methods=['POST'], endpoint='registry')
@login_required
def registry():
    # 是否使用 IP 代理
    use_ip_proxy = request.form['use_ip_proxy']
    with open('use_ip_proxy.txt', 'w', encoding='utf-8') as use_ip_proxy_f:
        use_ip_proxy_f.write(use_ip_proxy)
    # with open('document_plus/logger_result.txt', 'r+', encoding='utf-8') as result_f:
    #     result_f.truncate()
    #
    # with open('document_plus/number_status_result.txt', 'w', encoding='utf-8') as number_status_result_f:
    #     number_status_result_f.write("0")
    #
    # with open('document_plus/recode_status_result.txt', 'w', encoding='utf-8') as recode_status_result_f:
    #     recode_status_result_f.write("0")
    if os.path.exists("email_list_file.txt"):
        with open("email_list_file.txt", 'r', encoding='utf-8') as email_list_file_f:
            can_use = len(email_list_file_f.readlines())
        # 待执行的人物列表
        task_number.origin_detail_len = can_use
    with open("task_status.txt", 'w', encoding='utf-8') as stop_foo:
        stop_foo.write("start")
    result = {}
    # # 需要从request对象读取表单内容：
    # print(request.form)
    # count = request.form['count']
    with open('setting_prefix.txt', 'r', encoding='utf-8') as setting_prefix_f:
        prefix = setting_prefix_f.read()
    if prefix.__len__() == 0:
        result["status"] = "fail"
        result["msg"] = "尚未设置前缀！"
    else:
        start_registry()
        result["status"] = "ok"
        result["msg"] = "开始"
    return json.dumps(result)


@app.route('/stop_task', methods=['POST'], endpoint='stop_task')
@login_required
def stop_task():
    with open("task_status.txt", 'w', encoding='utf-8') as stop_foo:
        stop_foo.write("stop")
    return json.dumps({"status": True}, ensure_ascii=False)


@app.route('/complate_count', methods=['POST'], endpoint='complate_count')
@login_required
def complate_count():
    """
    检测完成的数量
    :return:
    """
    # $("#complete_time").text(data_split[0]);
    #                     $("#success_time").text(data_split[1]);
    # if os.path.exists(date_time_str + '_origin_account_detail.txt'):
    #     with open(date_time_str + '_origin_account_detail.txt', 'r', encoding='utf-8') as origin_detail_f:
    #         origin_detail_len = len(origin_detail_f.readlines())
    #     if origin_detail_len > 0:
    #         origin_detail_len = origin_detail_len - 1
    #     if os.path.exists(date_time_str + '_success_account_detail.txt'):
    #         with open(date_time_str + '_success_account_detail.txt', 'r', encoding='utf-8') as success_detail_f:
    #             success_detail_len = len(success_detail_f.readlines())
    #         success_rate = round(success_detail_len / origin_detail_len, 2) * 100
    #         result = str(origin_detail_len) + ',' + str(success_detail_len) + ',' + str(success_rate)
    #         return result
    #     else:
    #         return str(origin_detail_len) + ',0,0.00'
    # else:
    #     return '0,0,0.00'

    if os.path.exists(date_time_str + '_success_account_detail.txt'):
        with open(date_time_str + '_success_account_detail.txt', 'r', encoding='utf-8') as success_detail_f:
            success_detail_len = len(success_detail_f.readlines())
        if task_number.origin_detail_len >= 0:
            success_rate = round(success_detail_len / task_number.origin_detail_len, 2) * 100
            return str(task_number.origin_detail_len) + ',' + str(success_detail_len) + ',' + str(success_rate)
        else:
            return str(task_number.origin_detail_len) + ',0,0.00'
    else:
        return str(task_number.origin_detail_len) + ',0,0.00'


@app.route('/logger_register_table', methods=['POST'], endpoint='logger_register_table')
@login_required
def logger_register_table():
    if os.path.exists(date_time_str + '_origin_account_detail.txt'):
        with open(date_time_str + '_origin_account_detail.txt', 'r', encoding='utf-8') as account_detail_f:
            content = account_detail_f.readlines()
        # print(str(content))
        content_str = """<head><meta charset="UTF-8"><title>展示成功注册信息</title></head><body>"""
        content_str = content_str + '<br>'.join(content)
        content_str = content_str + '</body>'
        print(content_str)
        return content_str
    else:
        content_str = """<head><meta charset="UTF-8"><title>展示成功注册信息</title></head><body>"""
        content_str = content_str + '<br>暂无开始注册信息'
        content_str = content_str + '</body>'
        print(content_str)
        return content_str


@app.route('/reg_history_page_view', methods=['POST'], endpoint='reg_history_page_view')
@login_required
def reg_history_page_view():
    if os.path.exists(date_time_str + '_success_account_detail.txt'):
        with open(date_time_str + '_success_account_detail.txt', 'r', encoding='utf-8') as account_detail_f:
            content = account_detail_f.readlines()
        # print(str(content))
        content_str = """<head><meta charset="UTF-8"><title>展示成功注册信息</title></head><body>"""
        content_str = content_str + '<br>'.join(content)
        content_str = content_str + '</body>'
        print(content_str)
        return content_str
    else:
        content_str = """<head><meta charset="UTF-8"><title>展示成功注册信息</title></head><body>"""
        content_str = content_str + '<br>暂无成功注册信息'
        content_str = content_str + '</body>'
        print(content_str)
        return content_str


@app.route('/reg_download', methods=['POST'], endpoint='reg_download')
@login_required
def reg_download():
    if os.path.exists(date_time_str + '_success_account_detail.txt'):
        response = make_response(
            send_file(date_time_str + '_success_account_detail.txt', mimetype='text/csv', as_attachment=True))
        # response = make_response(content_str)
        response.headers["Content-Disposition"] = "attachment; filename=" + date_time_str + ".txt"
        return response
    else:
        content_str = """<head><meta charset="UTF-8"><title>展示成功注册信息</title></head><body>"""
        content_str = content_str + '<br>暂无成功注册信息'
        content_str = content_str + '</body>'
        print(content_str)
        return content_str


@app.route('/get_logger', methods=['POST'], endpoint='get_logger')
@login_required
def get_logger():
    syslog = 'syslog.txt'
    if os.path.exists(syslog):
        with open(syslog, 'r', encoding='utf-8') as log_foo:
            return '\n'.join(log_foo.readlines())
    else:
        return '尚未产生日志'


# from flask import make_response , send_file
# @app.route('/testdownload', methods=['GET'])
# def testdownload():
#     response = make_response(send_file("views.py"))
#     response.headers["Content-Disposition"] = "attachment; filename=views.py;"
#     return response

# p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
# out, err = p.communicate()
# out_line_str = ''
# err_line_str = ''
# if out:
#     if len(out) > 0:
#         for line in out.splitlines():
#             out_line_str = out_line_str + str(line, encoding="utf-8")

#         if "fail" in out_line_str:
#             print('fail:::'+out_line_str)
#         else:
#             print('sccess:::'+out_line_str)
#     else:
#         pass
# if err:
#     if len(err) > 0:
#         for line_err in err.splitlines():
#             err_line_str = err_line_str + str(line_err, encoding='utf-8')
#         print(err_line_str)
#     else:
#         pass


# return json.dumps(result, ensure_ascii=False)

# if "ok" in statusx:
#     result["status"] = "success"
#     result["usetime"] = str(usetimex)
#     print("result::" + str(result))
#     return json.dumps(result, ensure_ascii=False)
# else:
#     result["status"] = statusx
#     result["usetime"] = 0
#     return json.dumps(result, ensure_ascii=False)


if __name__ == '__main__':
    """
    Flask 单例微服务启动
    """
    system_log_clear()
    system_log('__main__ start server 端口号：80')
    # setup_logging(default_path="logging.json")
    app.run(host='0.0.0.0', port=80)
    app.run()
