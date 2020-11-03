from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import uuid
import time
import json
import time
import requests
import re
import random
import os
from io import BytesIO
import re

import requests
from requests.cookies import RequestsCookieJar

s = requests.session()
# from PIL import Image
# import math
# from bs4 import BeautifulSoup
import re

# 注意：以下设置将体现在 谷歌浏览器： 版本 74.0.3729.169（正式版本） （32 位），
# 以及selenium 谷歌客户端已经设置好，版本需要同步
# 用户参数设置区域，如果改变了账户名和密码，那么以下内容中如果是基于requests请求那么请求头和cookie设置需要重新设置
# 另外如果更换了爬虫服务的机器，那么也请重新设置请求头和cookie设置

# 以下单位皆为 秒
login_retry = 10  # 后台尝试登陆间隔次数
left = 594 - 110
top = 445 - 110

width = 1200
height = 700
delay = 1

#  基于起始位置参数设置所要截取的图片尺寸 （为了防止偏差，最好实际测试）
right = left + 115
bottom = top + 40

# 请求头和cookie设置
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

chrome_options = Options()
# 不弹出浏览器模式，不弹出浏览器模式默认网页size
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--user-agent=' + user_agent)
chrome_options.add_argument('--disable-infobars')

# chrome_options.add_argument('--proxy-server={}'.format(proxy))
# # 配置忽略ssl错误
# capabilities = DesiredCapabilities.CHROME.copy()
# capabilities['acceptSslCerts'] = True
# capabilities['acceptInsecureCerts'] = True
# browser = webdriver.Chrome(desired_capabilities=capabilities)
chrome_driver = '../Application/chromedriver.exe'  # 手动指定使用的浏览器位置
# chrome_driver = r"C:\Python37\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)


class Email126(object):
    def __init__(self):
        # self.session = requests.session()
        # self.cookies = requests.cookies.RequestsCookieJar()
        self.url_126 = 'http://www.126.com/index_alternate.htm'
        # self.login_action = 'https://mail.126.com/'
        self.login_username = ""
        self.login_password = ""
        # self.login_url2 = "https://mail.126.com/errorpage/error126.htm"

    # def cookie_fetch_126(self):
    #     main_header = {
    #         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    #         'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    #         'Connection': 'keep-alive'
    #     }

    # def login_126(self):
    #
    #     main_header = {
    #         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    #         'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    #         'Connection': 'keep-alive'
    #     }
    #     post_data = {'username': self.login_username, 'url2': self.login_url2, 'password': self.login_password}
    #     response = self.session.request('post',
    #                                     'https://mail.126.com/',
    #                                     data=post_data,
    #                                     headers=main_header,
    #                                     cookies=self.cookies,
    #                                     verify=False)  # 传递cookie
    #     # self.cookies.set('cookie-name', 'cookie-value', path='/', domain='.abc.com')  # 保存更新cookie
    #     self.session.cookies.update(response.cookies)
    #     # {"gid": "2498864890707537149", "type": 2, "sitekey": "6LerFqAUAAAAABMeByEoQX9u10KRObjwHf66-eya"}
    #     text = response.text

    def login_with_verify_picture(self, width, height):
        try:
            driver.set_window_size(width, height)
            driver.get(self.url_126)
            all_windows = driver.window_handles
            print('登录之前所有窗口', all_windows)
            cookies = driver.get_cookies()
            print("登录之前的cookie：%s " % str(cookies))
            print("登录之前的url：%s " % driver.current_url)

            # xpath 参数设置
            tap_xpath_login_email_account = '//*[@id="lbNormal"]'
            input_xpath_username = '//*[@id="idInput"]'
            input_xpath_password = '//*[@id="pwdInput"]'
            checkbox_xpath_ten_days = '//*[@id="lfAutoLogin"]/b'
            enter_xpath = '//*[@id="loginBtn"]'

            # 访问页面，填写xpath
            element_input = driver.find_element_by_xpath(tap_xpath_login_email_account)
            element_input.click()
            element_input = driver.find_element_by_xpath(input_xpath_username)
            element_input.clear()
            element_input.send_keys(self.login_username)
            element_input = driver.find_element_by_xpath(input_xpath_password)
            element_input.clear()
            element_input.send_keys(self.login_password)
            element_input = driver.find_element_by_xpath(checkbox_xpath_ten_days)
            element_input.click()

            # element.send_keys(Keys.RETURN)
            element_enter = driver.find_element_by_xpath(enter_xpath)
            element_enter.click()
            # 获取当前窗口
            login_after_window = driver.current_window_handle
            # 默认第一个窗口
            print('点击登陆之后的窗口信息', login_after_window)
            # 第二次获取所有窗口后发现 多了一个
            login_after_all_windows = driver.window_handles
            print('登录之 --后-- 所有窗口', login_after_all_windows)
            cookies = driver.get_cookies()
            print("登录之后的cookie：%s " % str(cookies))
            login_after_current_url = driver.current_url
            print("登录之后的url：%s " % login_after_current_url)

            print(driver.page_source)
            # quit_button = EC.presence_of_element_located(
            #     (By.XPATH, "/html/body/div/div[1]/div[2]/div/ul[2]/li[8]/div/a/span"))
            # if quit_button:
            #     ready_search = True
            # else:
            #     pass

            # 查找邮件
            span_xpath_recive_email = '//*[@id="_mail_component_27_27"]/span[2]'
            element_enter = driver.find_element_by_xpath(span_xpath_recive_email)

            element_enter.click()

            cookies = driver.get_cookies()
            print("点击收件箱的cookie：%s " % str(cookies))
            with open('cookies.txt', 'w', encoding='utf-8') as sele_cookie_foo:
                json.dump(cookies, sele_cookie_foo)
            login_after_current_url = driver.current_url
            print("点击收件箱的url：%s " % login_after_current_url)

            match_group = re.match(r'.*?sid=(.*?)&df=mail.*?', str(login_after_current_url),
                                   re.M | re.I | re.S | re.IGNORECASE)
            sid = match_group.group(1)
            print('sid : ', sid)
            # 这里我们使用cookie对象进行处理
            jar = RequestsCookieJar()
            with open("cookies.txt", "r") as fp:
                cookies = json.load(fp)
                for cookie in cookies:
                    jar.set(cookie['name'], cookie['value'])
            print('jar ::', jar)
            # steam_mail = 'https://mail.126.com/js6/s?sid='+sid+'&func=mbox:readMessage&l=read&action=read'
            steam_mail = 'https://mail.126.com/js6/s?sid=' + sid + '&func=mbox:readMessage&LeftNavRecieveMailClick=1&l=read&action=read'
            print('steam_mail ::', steam_mail)
            s.headers = {"User-Agent": user_agent}
            r = s.post(steam_mail, cookies=jar)
            print(r.status_code)
            print(r.url)
            print(r.text)

            url = 'http://ocr.xinby.cn/api.php?user=15847433555&pass=cuizhi8899&act=mail&type=read&email=mdqnqi@126.com&pwd=jqy8o8laf&title=Steam&format=html'
            response = requests.get(url)  # 传递cookie

            print(response.text)
            match_group = re.match(
                r'.*?https%3A%2F%2Fstore.steampowered.com%2Faccount%2Fnewaccountverification%3F(.*?)&amp;keyfrom=jumper.in&amp;c=TRUE&amp;j=1&amp.*?">',
                str(response.text), re.M | re.I | re.S | re.IGNORECASE)
            base_url = 'https://store.steampowered.com/account/newaccountverification?'
            print(match_group.group(1))
            stoken_creationid = str(match_group.group(1)).replace('%3D', '=').replace('%26', '&')
            base_url = base_url + stoken_creationid
            print('base_url :::', base_url)
            driver.get(base_url)
            # res = requests.get(base_url)
            # print(res.text)

            # 'https://mail.126.com/js6/read/readhtml.jsp?mid=104:1tbiaBt7H1pD-H9hdAAAsY&userType=browser&font=15&color=138144'

            # 'https://mail.126.com/js6/s?sid=ZAREiCddiephgyfkkJddhCwTHXNveZRL&func=mbox:readMessage&LeftNavRecieveMailClick=1&l=read&action=read'
            # 'https://mail.126.com/js6/main.jsp?sid=LBXITQzzAfAVpnfJRHzzkqKyDPNPpBRz&df=mail126_letter#module=mbox.ListModule%7C%7B%22fid%22%3A1%2C%22order%22%3A%22date%22%2C%22desc%22%3Atrue%7D'

            # xpath_email_list = '//*[@id="_dvModuleContainer_mbox.ListModule_2"]'
            # element_class_click = driver.find_element_by_xpath(xpath_email_list)
            # element_class_click.click()
            # content_xpath = '//*[@id="dvContentContainer"]'
            # content_xpath_page_source = driver.find_element_by_xpath(content_xpath)
            # text = content_xpath_page_source.find_element_by_name()
            # print(text)
            # import time
            # time.sleep(3)
            # 等待3秒进行加载....
            # print('等待3秒进行加载....')
            # match_group = re.match(r'<div class="rF0 nui-txt-flag0 ik0" tabindex="0" id="(.*?)" role="link"',
            #                        text, re.M | re.I | re.S | re.IGNORECASE)
            # email_id = match_group.group(1)
            # html = driver.page_source
            # time.sleep(5)
            # print(html)
            # match_result = re.findall(r'<div class="rF0 nui-txt-flag0 ik0" tabindex="0" id="(.*?)" role="link"', html,
            #                           re.M | re.I | re.S | re.IGNORECASE)
            # email_id = match_result[0]
            # ------
            # steam_xpath_in_first_list = '//*[@id="' + email_id + '"]/div'
            # element_click = driver.find_element_by_xpath(steam_xpath_in_first_list)
            # element_click.click()

            # login_after_all_windows = driver.window_handles
            # print('点击-> 收件 -> steam 之后的 所有窗口', login_after_all_windows)
            # cookies = driver.get_cookies()
            # print("点击-> 收件 -> steam 之后的 cookie：%s " % str(cookies))
            # login_after_current_url = driver.current_url
            # print("点击-> 收件 -> steam 之后的 url：%s " % login_after_current_url)
            #
            # release_xpath_in_content = '//*[@id="content"]/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr/td/a/span'
            # element_click = driver.find_element_by_xpath(release_xpath_in_content)
            # element_click.click()
            #
            # print("邮箱验证完成....")

        except Exception as first_img_code_localutils_e:
            print("异常信息：%s " % str(first_img_code_localutils_e))
            raise first_img_code_localutils_e


if __name__ == '__main__':
    emial126 = Email126()
    emial126.login_username = 'mdqnqi'
    emial126.login_password = 'jqy8o8laf'
    emial126.login_with_verify_picture(width, height)
