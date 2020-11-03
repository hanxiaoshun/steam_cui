import threading
import time
import queue
import os
from code.controller import Controller
import random
from code.utils import *

ctrl = Controller()
# 获得线程锁
# thread_lock = threading.Lock()


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, email, date_time_str, proxy=None):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.email = email
        self.date_time_str = date_time_str
        self.proxy = proxy

    def run(self):
        # print("开启线程： " + self.name)
        # 获取锁，用于线程同步
        # threadLock.acquire()
        start_worker(self.name, self.counter, self.email, self.date_time_str, self.threadID, self.proxy)
        # 释放锁，开启下一个线程
        # threadLock.release()


def start_worker(threadName, delay, email, date_time_str, threadID, proxy):
    system_log(str(threadID) + '线程执行:' + threadName + ',任务邮件：' + email)
    with open("email_list_file.txt", 'r', encoding='utf-8') as email_can_use_f:
        email_use = email_can_use_f.readlines()
    with open("email_list_file_already_use.txt", 'r', encoding='utf-8') as email_list_file_already_use_f:
        email_already_use = email_list_file_already_use_f.readlines()

    with open('setting_prefix.txt', 'r', encoding='utf-8') as setting_prefix_f:
        prefix = setting_prefix_f.read().strip().replace('\t', '').replace('\n', '')
    name_prefix = prefix + str(threadID)
    time.sleep(delay)
    if email not in email_already_use:
        if len(str(email)) > 0:
            email_already_use.append(email)
            email_use.remove(email)
            # '*mdqnqi@126.com----jqy8o8laf'
            email_split = str(email).split('----')
            ctrl.need_email_address = email_split[0].strip().replace('\t', '').replace('\n', '')
            ctrl.email_pwd = email_split[1].strip().replace('\t', '').replace('\n', '')
            ctrl.steam_account_name = name_prefix
            ramdom_seed = ['W', 'R', 'T', 'Y', 'Ys', 'wq', 'EE', '2w', '45', 'frvb', '6YGH', '2sgy', '234',
                           'df', 'G', 'GF', 'HTS', 'EDG', 'RFDFD', 'Z', 'okz', 'dsa', 'WF3', '354fD',
                           '4DT', 'ERT', 'vgt', '5Tws', 'TD4']
            seed = random.choice(ramdom_seed)
            ctrl.steam_password = name_prefix + seed
            date_time_detail_str = str(time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            detail_str = ctrl.need_email_address + \
                         '----' + ctrl.email_pwd + \
                         '----' + ctrl.steam_account_name + \
                         '----' + ctrl.steam_password + \
                         '----' + date_time_detail_str + '\n'
            system_log(detail_str)
            with open(date_time_str + '_origin_account_detail.txt', 'a',
                      encoding='utf-8') as account_detail_f:
                account_detail_f.write(detail_str)
            ctrl.start(date_time_str, proxy)
        else:
            pass
        with open("email_list_file.txt", 'r+', encoding='utf-8') as email_can_use_f:
            email_can_use_f.truncate()
        with open("email_list_file_already_use.txt", 'r+',
                  encoding='utf-8') as email_list_file_already_use_f:
            email_list_file_already_use_f.truncate()
        # 对写操作进行加锁
        # thread_lock.locked()
        with open("email_list_file.txt", 'a', encoding='utf-8') as email_can_use_f:
            for i in email_use:
                email_can_use_f.write(i + '\n')
        with open("email_list_file_already_use.txt", 'a',
                  encoding='utf-8') as email_list_file_already_use_f:
            for i in email_already_use:
                email_list_file_already_use_f.write(i + '\n')
        # thread_lock.release()
    else:
        pass


# threadLock = threading.Lock()
def start_thread_queue(date_time_str):
    with open("email_list_file.txt", 'r', encoding='utf-8') as email_can_use_f:
        email_use = email_can_use_f.readlines()
    ready_queue = queue.LifoQueue()
    [ready_queue.put(x) for x in email_use if x.strip().replace('\t', '').replace('\n', '').__len__() > 0]
    with open('use_ip_proxy.txt', 'r', encoding='utf-8') as use_ip_proxy_f:
        use_ip_proxy = use_ip_proxy_f.read()
    if 'yes' in use_ip_proxy:
        with open("file_ip_list.txt", 'r', encoding='utf-8') as file_ip_list_f:
            ip_list = file_ip_list_f.readlines()
    else:
        pass
    time.sleep(1)
    threads = []
    threads.clear()
    with open("file_ip_list.txt", 'r', encoding='utf-8') as file_ip_list_f:
        ip_list = file_ip_list_f.readlines()
    for i in range(email_use.__len__()):
        if 'yes' in use_ip_proxy:
            proxy_ip = random.choice(ip_list).strip().replace('\t', '').replace('\n', '')
        else:
            proxy_ip = None
        time.sleep(25)
        system_log('')
        # 灌入10个线程
        if ready_queue.empty():
            # 如果队列为空了则跳出去
            break
        else:
            # 创建新线程
            if os.path.exists("file_ip_list_already_use.txt"):
                while True:
                    with open("file_ip_list_already_use.txt", 'r', encoding='utf-8') as file_ip_list_already_use_f:
                        if proxy_ip:
                            if proxy_ip not in file_ip_list_already_use_f.readlines():
                                with open("file_ip_list_already_use.txt", 'a',
                                          encoding='utf-8') as file_ip_list_already_use_w_f:
                                    file_ip_list_already_use_w_f.write(proxy_ip + '\n')
                                break
                            else:
                                proxy_ip = random.choice(ip_list).strip().replace('\t', '').replace('\n', '')
                        else:
                            proxy_ip = None
            else:
                pass
            system_log("-- proxy_ip --" + proxy_ip)
            if 'yes' in use_ip_proxy:
                thread_body = myThread(i, "Thread-" + str(i), 1.5, ready_queue.get(), date_time_str, proxy_ip)
                threads.append(thread_body)
            else:
                thread_body = myThread(i, "Thread-" + str(i), 1.5, ready_queue.get(), date_time_str, None)
                threads.append(thread_body)
    # 开启新线程
    # 添加线程到线程列表
    # 等待所有线程完成
    for t in threads:
        time.sleep(1.5)
        t.start()
    for t in threads:
        t.join()
    print("退出主线程")

# if __name__ == '__main__':
#     whatsapp = 'https://www.whatsapp.com'
#     start_thread_queue()
