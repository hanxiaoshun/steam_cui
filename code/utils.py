import time


def system_log(log_str):
    """
    写入相关的日志信息
    :return:
    """
    date_time_current = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    with open('syslog.txt', 'a', encoding='utf-8') as log_foo:
        log_foo.write(date_time_current + ' ' + log_str + '\n')


def system_log_clear():
    with open('syslog.txt', 'r+', encoding='utf-8') as log_foo:
        log_foo.truncate()
