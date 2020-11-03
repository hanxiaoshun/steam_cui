import requests
import json
import logging
import re
import time
from code.python3_email_recive_object2 import EmailParse
from code.utils import *

email_parse = EmailParse()
requests.packages.urllib3.disable_warnings()
url = 'https://recaptcha.net/recaptcha/api2/reload?k=6LerFqAUAAAAABMeByEoQX9u10KRObjwHf66-eya'


class Recaptcha(object):
    def __init__(self):
        """
        初始化参数信息
        """
        self.session = requests.session()
        self.cookies = requests.cookies.RequestsCookieJar()
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        self.origin = 'https://store.steampowered.com'
        self.host = 'store.steampowered.com'
        self.language = 'zh-CN,zh;q=0.9'
        self.first_referer = 'https://store.steampowered.com/join/?redir=about'

        self.type = ''
        self.captchagid_gid = ''
        self.captcha_text = ''
        self.creationid = ''

        self.user = '15847433555'
        self.password = 'cuizhi8899'
        self.token = "\t4eb42929b6e6b61f4ab7c7dbfa011e93"
        self.act = 'mail'
        self.type = 'read'
        self.s = 'ptl3gi@126.com'
        self.email_pwd = 'utqswjoma'
        self.email_title = 'Steam'
        self.format = 'html'

    def login_moyun(self):
        """
        登录魔云
        :return:
        """
        system_log("开始登录魔云打码平台....")
        main_header_send = {
            'content-type': 'application/x-www-form-urlencoded',
            'User-Agent': self.user_agent
        }

        post_data_send = {
            "user": "15847433555",
            "pass": "cuizhi8899",
            "dev_id": "1",
            "act": "login"
        }

        response_send = self.session.request('post',
                                             'https://ocr.xinby.cn/api.php',
                                             data=post_data_send,
                                             headers=main_header_send,
                                             verify=False)  # 传递cookie
        print(" login 魔云.text :: ", response_send.text)
        login_moyun = json.loads(response_send.text)
        if login_moyun['code'] == 1:
            if login_moyun["data"]['token']:
                print("魔云 login success")
                system_log("魔云 login success")
            else:
                print("魔云 login fail")
                system_log("魔云 login fail")
        else:
            print("魔云 login fail")
        # """
        # {
        #     "code": 1,
        #     "data": {
        #         "id": 11694,
        #         "user": "15847433555",
        #         "token": "4eb42929b6e6b61f4ab7c7dbfa011e93",
        #         "type": 0,
        #         "bp": "48076.00"
        #     }
        # }
        # """

    def get_captcha_text(self, sitekey):
        """
        请求打码结果
        :return:
        """
        main_header_send = {
            'content-type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.kancloud.cn',
            'Referer': 'https://www.kancloud.cn/jeaxnew/mocloud/1037431',
            'User-Agent': self.user_agent
        }

        post_data_send = {
            "user": self.user,
            "pass": self.password,
            "dev_id": 1,
            "act": "recaptcha",
            "type": "post",
            "k": sitekey,
            "referer": "https://store.steampowered.com//join//?redir=about\\/"
        }

        response_send = self.session.request('post',
                                             'https://ocr.xinby.cn/api.php',
                                             data=post_data_send,
                                             headers=main_header_send,
                                             verify=False)  # 传递cookie
        # self.cookies.set('cookie-name', 'cookie-value', path='/', domain='.abc.com')  # 保存更新cookie
        self.session.cookies.update(response_send.cookies)
        print(" response_send.text :: ", response_send.text)
        # {"code":1,"data":{"hash":"15173492","id":"15173492","id_info":"后期将移除id请使用hash"}}
        json_data = json.loads(response_send.text)
        if json_data['code'] == 1:
            get_time = 12
            while get_time > 0:
                wait_time = 5
                while wait_time > 0:
                    time.sleep(1)
                    print("第" + str(get_time) + "轮等待" + str(wait_time))
                    wait_time = wait_time - 1

                data = json_data['data']
                hash = data['hash']

                main_header_get = {
                    "content-type": "application/x-www-form-urlencoded",
                    'User-Agent': self.user_agent
                }
                post_data_get = {
                    "user": self.user,
                    "pass": self.password,
                    "dev_id": 1,
                    "act": "recaptcha",
                    "type": "res",
                    "hash": hash
                }

                response_get = self.session.request('post',
                                                    'https://ocr.xinby.cn/api.php',
                                                    data=post_data_get,
                                                    headers=main_header_get,
                                                    verify=False)
                # {
                #     "code": 1,
                #     "data": {
                #         "recaptcha": "03AOLTBLSrwMPJMLwW--VGhO1F_nDBYaYnvzQXFWuwGcoWPSp8zEjR5EnxTIl00qvNUi6uDYjZg43QLlh3HMldcfzK7VaCdjyBdVvEDXuvXMc4F8COoButmJWsYAccvU5SSm4XQZrZay5MQXpc1tGOt6wWqmMmqf072LRCvklTcrCFWWkZR5JBcX1ksPlSm43HjlWHXL9i2GpMXiIHWNVOAH9_m9FzZQ_LAhTdWk5YS2DhGxy9p6aViQGoHgZy5XUOr2jLVujnbPyIN6IQkG7Vemg9VwYkKW0iO8dD0oPXhHVQM8fxj4U-wpfVkMGBA_X8Q-YXtXv0UfxBmkmaM-oTCQTClo_DyzV-let6JSCwkHRg7qQrtSbgI2ZCsAxao9anCIyqdN8mgYC_9bixrM9BFfReF9xwlRcGb7DHwk2X8BG8dJPvHNeMnfsedzfsHGaI4WqoOAN4oyMzBIvbI-plPM0izevS74GiPaTzFzkWaNEWauDqZHw2RFbjYCpYpG1STId3oYZ2KcW3",
                #         "hash": 15090250,
                #         "id": 15090250,
                #         "id_info": "后期将移除id请使用hash"
                #     }
                # }
                print('--- post_data_get--', response_get.text)
                json_data_get = json.loads(response_get.text)
                # {"code": -1888, "errmsg": "processing"}
                if json_data_get['code'] == -1888:
                    get_time = get_time - 1
                else:
                    if json_data_get['code'] == 1:
                        data = json_data_get['data']
                        hash = data['hash']
                        recaptcha = data['recaptcha']
                        self.captcha_text = recaptcha
                        print('type:', self.type)
                        print('captchagid_gid:', self.captchagid_gid)
                        print('captcha_text:', self.captcha_text)
                        print('creationid:', self.creationid)
                        break
                    else:
                        get_time = get_time - 1


class SteamRegistry(object):
    def __init__(self):
        """
        初始化参数信息
        """
        self.session = requests.session()
        self.cookies = requests.cookies.RequestsCookieJar()
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        self.origin = 'https://store.steampowered.com'
        self.host = 'store.steampowered.com'
        self.language = 'zh-CN,zh;q=0.9'
        self.first_referer = 'https://store.steampowered.com/join/?redir=about'

        self.type = ''
        self.captchagid_gid = ''
        self.captcha_text = ''
        self.creationid = ''
        self.count = 1
        self.date_time_str = ''
        self.user = '15847433555'
        self.password = 'cuizhi8899'
        self.token = "\t4eb42929b6e6b61f4ab7c7dbfa011e93"
        self.act = 'mail'
        self.type = 'read'
        self.email_address = 'd8abvu@126.com'
        self.email_pwd = 't0n5u8tiw'
        self.email_title = 'Steam'
        self.format = 'html'

        self.steam_accountname = ''
        self.steam_password = ''
        self.email_active_status = False

    def cookie_fetch(self):
        """
        建立链接，保持cookie
        :return:
        """
        main_header = {
            # 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            'User-Agent': self.user_agent,
            'Origin': self.origin,
            'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': self.language,
            'Connection': 'keep-alive',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Host': 'store.steampowered.com',
            'Referer': self.first_referer
        }
        response = self.session.request('GET', url=self.first_referer, headers=main_header, cookies=self.cookies)
        # self.cookies.set('cookie-name', 'cookie-value', path='/', domain='.abc.com')  # 保存更新cookie
        self.session.cookies.update(response.cookies)

    def recaptcha(self):
        """
        获得打码所需的 sitekey
        :return:
        """
        main_header = {
            'User-Agent': self.user_agent,
            'Origin': self.origin,
            'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': self.language,
            'Connection': 'keep-alive',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Host': 'store.steampowered.com',
            'Referer': self.first_referer
        }
        post_data = {'count': self.count}
        response = self.session.request('post',
                                        'https://store.steampowered.com/join/refreshcaptcha/',
                                        data=post_data,
                                        headers=main_header,
                                        cookies=self.cookies,
                                        verify=False)  # 传递cookie
        # self.cookies.set('cookie-name', 'cookie-value', path='/', domain='.abc.com')  # 保存更新cookie
        self.session.cookies.update(response.cookies)
        # {"gid": "2498864890707537149", "type": 2, "sitekey": "6LerFqAUAAAAABMeByEoQX9u10KRObjwHf66-eya"}
        json_data = json.loads(response.text)
        self.captchagid_gid = json_data['gid']
        self.type = json_data['type']
        self.sitekey = json_data['sitekey']
        print('type:', self.type)
        print('captchagid_gid:', self.captchagid_gid)
        print('captcha_text:', self.captcha_text)
        print('creationid:', self.creationid)

    def ajaxverifyemail(self):
        """
        请求creationid
        :return:
        """

        main_header = {
            'User-Agent': self.user_agent,
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': self.language,
            'Connection': 'keep-alive',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Host': 'store.steampowered.com',
            'Origin': 'https://store.steampowered.com',
            'Referer': 'https://store.steampowered.com/join',
            'X-Requested-With': 'XMLHttpRequest'
        }
        method = 'post'
        url = 'https://store.steampowered.com/join/ajaxverifyemail'
        post_data = {'email': self.email_address,
                     'captchagid': self.captchagid_gid,
                     'captcha_text': self.captcha_text}
        print('post_data:: ', str(post_data))
        response = self.session.request(method,
                                        url,
                                        data=post_data,
                                        headers=main_header,
                                        cookies=self.cookies,
                                        verify=False)  # 传递cookie
        # self.cookies.set('cookie-name', 'cookie-value', path='/', domain='.abc.com')  # 保存更新cookie
        # {"success":1,
        # "sessionid":"7971650214778562899",
        # "details":"\u521b\u5efa\u60a8\u7684 Steam \u5e10\u6237\u65f6\u53d1\u751f\u4e86\u4e00\u4e2a\u9519\u8bef\uff0c\u8bf7\u7a0d\u540e\u518d\u8bd5\u3002"}
        print('-- ajaxverifyemail url--', response.url)

        print('-- ajaxverifyemail --', response.text)
        json_data = json.loads(response.text)
        success = json_data['success']
        sessionid = json_data['sessionid']
        details = json_data['details']
        self.creationid = json_data['sessionid']
        # creationid: 7971650214778562899
        self.session.cookies.update(response.cookies)
        print('type:', self.type)
        print('captchagid_gid:', self.captchagid_gid)
        print('captcha_text:', self.captcha_text)
        print('creationid:', self.creationid)

    def email_active(self):
        """
        激活邮件
        :return:
        """
        try_time = 12
        while try_time > 0:
            url = 'http://ocr.xinby.cn/api.php?' \
                  + 'user=' + self.user \
                  + '&pass=' + self.password \
                  + '&act=mail&type=read' \
                  + '&email=' + self.email_address \
                  + '&pwd=' + self.email_pwd \
                  + '&title=' + self.email_title \
                  + '&format=html'

            print("\n -- url --" + url)
            system_log('取邮件验证 url :  ' + "\n -- url --" + url)
            response = requests.get(url)  # 传递cookie
            response_json = json.loads(response.text)
            # {"code": -1002, "errmsg": "未获取到邮件"}
            print('取到邮件返回:  ' + response.text)
            system_log('取到邮件返回:  ' + response.text)
            print("取到邮件 第：：", str(try_time))
            system_log("取到邮件 第：：" + str(try_time))
            if response_json['code'] == -1002:
                print(response_json['errmsg'])
                try_time = try_time - 1
                time.sleep(10)
                email_active_time = 7
                while email_active_time > 7:
                    time.sleep(1)
                    print('try_time: ' + try_time + ', email_active_time:' + str(email_active_time))
                    system_log('try_time: ' + try_time + ', email_active_time:' + str(email_active_time))
                    email_active_time -= 1
            else:
                logging.info("\n -- response.text --" + response.text)
                match_group = re.match(
                    r'.*?https%3A%2F%2Fstore.steampowered.com%2Faccount%2Fnewaccountverification%3F(.*?)&amp;keyfrom=jumper.in&amp;c=TRUE&amp;j=1&amp.*?">',
                    str(response.text), re.M | re.I | re.S | re.IGNORECASE)
                base_url = 'https://store.steampowered.com/account/newaccountverification?'
                stoken_creationid = str(match_group.group(1)).replace('%3D', '=').replace('%26', '&')
                logging.info("\n -- stoken_creationid --" + stoken_creationid)
                base_url = base_url + stoken_creationid
                logging.info("\n -- base_url --" + base_url)
                print('base_url :::', base_url)
                res = requests.get(base_url)
                print(res.text)
                print('type:', self.type)
                print('captchagid_gid:', self.captchagid_gid)
                print('captcha_text:', self.captcha_text)
                print('creationid:', self.creationid)
                try_time = 0
                self.email_active_status = True

    def ajaxcheckemailverified(self):
        """
        请求和响应注册表单页面
        :return:
        """
        # try_time = 12
        # while try_time > 0:
        main_header = {
            'User-Agent': self.user_agent,
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': self.language,
            'Connection': 'keep-alive',
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Host': 'store.steampowered.com',
            'Origin': 'https://store.steampowered.com',
            'Referer': 'https://store.steampowered.com/join',
            'X-Requested-With': 'XMLHttpRequest'
        }
        post_data = {'creationid': self.creationid}
        response = self.session.request('post',
                                        'https://store.steampowered.com/join/ajaxcheckemailverified',
                                        data=post_data,
                                        headers=main_header,
                                        cookies=self.cookies,
                                        verify=False)  # 传递cookie
        # self.cookies.set('cookie-name', 'cookie-value', path='/', domain='.abc.com')  # 保存更新cookie
        self.session.cookies.update(response.cookies)
        print(response.text)
        system_log('请求和响应注册表单页面: ' + response.text)
        # if response.text != '36':
        #     print("邮箱验证结果", response.text)
        #     print('type:', self.type)
        #     print('captchagid_gid:', self.captchagid_gid)
        #     print('captcha_text:', self.captcha_text)
        #     print('creationid:', self.creationid)
        #     try_time = 0
        # else:
        #     print('type:', self.type)
        #     print('captchagid_gid:', self.captchagid_gid)
        #     print('captcha_text:', self.captcha_text)
        #     print('creationid:', self.creationid)
        #     try_time = try_time - 1

    def createaccount(self):
        """
        注册账号
        https://store.steampowered.com/join/createaccount/
        :return:
        """
        main_header = {
            'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            # 'Content-Length': 111,
            'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'store.steampowered.com',
            'Origin': 'https://store.steampowered.com',
            'Referer': 'https://store.steampowered.com/join/completesignup?redir=about\/&creationid=' + str(
                self.creationid),
            'User-Agent': self.user_agent,
            'X-Prototype-Version': '1.7',
            'X-Requested-With': 'XMLHttpRequest'
        }
        post_data = {'accountname': self.steam_accountname,
                     'password': self.steam_password,
                     'count': self.count,
                     'lt': 0,
                     'creation_sessionid': self.creationid,
                     'embedded_appid': 0}
        response = self.session.request('post',
                                        'https://store.steampowered.com/join/createaccount/',
                                        data=post_data,
                                        headers=main_header,
                                        cookies=self.cookies,
                                        verify=False)  # 传递cookie
        print(response.text)
        b_status = json.loads(response.text)
        system_log('注册账号，返回码: ' + response.text)
        # '{"bSuccess":false,"bInSteamClient":false}'
        if b_status['bSuccess'] == 'false':
            system_log('注册账号，注册失败' + response.text)
        else:
            self.session.cookies.update(response.cookies)
            date_time_detail_str = str(time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            detail_str = self.email_address + \
                         '----' + self.email_pwd + \
                         '----' + self.steam_accountname + \
                         '----' + self.steam_password + \
                         '----' + date_time_detail_str + '\n'
            with open(self.date_time_str + '_success_account_detail.txt', 'a', encoding='utf-8') as account_detail_f:
                account_detail_f.write(detail_str)
            system_log('注册账号，注册成功' + response.text)

# if __name__ == '__main__':
#     accountname = 'asdasadsfgs1234'
#     password = 'asdassdddddfgWEs1234'
#     email_address = 'qadu40@126.com'
#     email_pwd = 'pcz9m64jl'
#
#     with open('syslog.txt', 'w', encoding='utf-8') as log_foo:
#         date_time_current = str(time.strftime(
#             '%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#         log_foo.write(date_time_current + ' ' + '__main__ start server')
#     recaptcha = Recaptcha()
#     recaptcha.email_address = email_address
#     recaptcha.email_pwd = email_pwd
#     recaptcha.login_moyun()
#
#     print("启动项目！...")
#     steam = SteamRegistry()
#     steam.email_address = email_address
#     steam.email_pwd = email_pwd
#     steam.steam_accountname = accountname
#     steam.steam_password = password
#
#     print("访问登录，注册页面...")
#     time.sleep(2)
#     steam.cookie_fetch()
#     print("reload 验证码！...")
#     time.sleep(3)
#     steam.recaptcha()
#     print("获取验证码的字串！...")
#     time.sleep(2)
#     recaptcha.get_captcha_text(steam.sitekey)
#     steam.captcha_text = recaptcha.captcha_text
#     if steam.captcha_text != '':
#         print("发送邮箱验证！...")
#         time.sleep(2)
#         steam.ajaxverifyemail()
#         print("点击邮箱激活！...")
#         time.sleep(2)
#         steam.email_active()
#         print("验证邮箱激活结果！...")
#         time.sleep(2)
#         if steam.email_active_status:
#             steam.ajaxcheckemailverified()
#             print("开始注册！...")
#             steam.createaccount()
