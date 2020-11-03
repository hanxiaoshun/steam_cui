from code.registry import *
from code.utils import *


class Controller(object):
    """
    控制层
    """

    def __init__(self):
        self.steam_account_name = ''
        self.steam_password = ''
        self.need_email_address = ''
        self.email_pwd = ''

    def start(self, date_time_str, proxy):
        """后台进程开始"""
        try:
            recaptcha = Recaptcha()
            recaptcha.email_address = self.need_email_address
            recaptcha.email_pwd = self.email_pwd
            recaptcha.login_moyun()
            print("启动项目！...")
            system_log("启动项目！...")
            steam = SteamRegistry()
            steam.email_address = self.need_email_address
            steam.email_pwd = self.email_pwd
            steam.steam_accountname = self.steam_account_name
            steam.steam_password = self.steam_password
            steam.date_time_str = date_time_str
            print("访问登录，注册页面...")
            system_log("访问登录，注册页面...")
            time.sleep(2)
            steam.cookie_fetch(proxy)
            print("reload 验证码！...")
            system_log("reload 验证码！...")
            time.sleep(3)
            steam.recaptcha(proxy)
            print("获取验证码的字串！...")
            system_log("获取验证码的字串！...")
            time.sleep(2)
            recaptcha.get_captcha_text(steam.sitekey)
            steam.captcha_text = recaptcha.captcha_text
            if steam.captcha_text != '':
                print("发送邮箱验证！...")
                system_log("发送邮箱验证！...")
                time.sleep(2)
                steam.ajaxverifyemail(proxy)
                print("点击邮箱激活！...")
                system_log("点击邮箱激活！...")
                time.sleep(2)
                steam.email_active(proxy)
                print("验证邮箱激活结果！...")
                system_log("验证邮箱激活结果！...")
                time.sleep(2)
                if steam.email_active_status:
                    steam.ajaxcheckemailverified(proxy)
                    print("开始注册！...")
                    system_log("开始注册！...")
                    steam.createaccount(proxy)
                else:
                    print('邮箱激活失败！')
                    system_log("邮箱激活失败！...")

        except Exception as  start_steam_e:
            print(f"start_steam_e: {start_steam_e}")
            raise start_steam_e
