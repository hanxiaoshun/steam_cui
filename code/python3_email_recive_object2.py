import poplib
import random
from email.header import decode_header
from email.parser import Parser
from email.utils import parseaddr
from code.utils import *
import requests
import re


def decodeMsgHeader(header):
    """
    解码头文件
    :param header: 需解码的内容
    :return:
    """
    value, charset = decode_header(header)[0]
    if charset:
        value = value.decode(charset)
    return value


def decodeBody(msgPart):
    """
    解码内容
   :param msgPart: 邮件某部分
    """
    contentType = msgPart.get_content_type()  # 判断邮件内容的类型,text/html
    textContent = ""
    if contentType == 'text/plain' or contentType == 'text/html':
        content = msgPart.get_payload(decode=True)
        charset = msgPart.get_charset()
        if charset is None:
            contentType = msgPart.get('Content-Type', '').lower()
            position = contentType.find('charset=')
            if position >= 0:
                charset = contentType[position + 8:].strip()
        if charset:
            textContent = content.decode(charset)
    return textContent


class EmailParse(object):
    def __init__(self):
        """POP的服务器信息"""
        self.popHost = "pop.126.com"
        self.userAdr = "bufandaojia20886@126.com"
        self.userPwd = "qiaotuanbixie"
        self.pop3Server = None

        self.messageCount = None
        self.mailboxSize = None

        self.response = None
        self.msgNumOctets = None
        self.octets = None

        self.parse_url = ''
        self.parse_status = ''

        self.messageObject = None

    def create_pop3(self):
        try:
            """ 创建POP3对象，添加用户名和密码"""
            self.pop3Server = poplib.POP3(self.popHost)
            self.pop3Server.user(self.userAdr)
            self.pop3Server.pass_(self.userPwd)
        except Exception as create_pop3_e:
            raise create_pop3_e

    def get_count_size(self):
        """获取邮件数量和占用空间"""
        try:
            self.messageCount, self.mailboxSize = self.pop3Server.stat()
            print("邮件数量...start")
            print(self.messageCount, self.mailboxSize)
            print("邮件数量...end")
            """获取邮件请求返回状态码、每封邮件的字节大小(b'第几封邮件 此邮件字节大小')、"""
            self.response, self.msgNumOctets, self.octets = self.pop3Server.list()
        except Exception as get_count_size_e:
            raise get_count_size_e

    def get_email_object(self):
        """ 获取任意一封邮件的邮件对象【第一封邮件的编号为1，而不是0】"""
        # msgIndex = random.randint(1, messageCount)
        # print(msgIndex)
        # 获取第msgIndex封邮件的信息
        try:
            response, msgLines, octets = self.pop3Server.retr(self.messageCount)
            # msgLines中为该邮件的每行数据,先将内容连接成字符串，再转化为email.message.Message对象
            msgLinesToStr = b"\r\n".join(msgLines).decode("utf8", "ignore")
            self.messageObject = Parser().parsestr(msgLinesToStr)
            print('-0----')
            print(type(self.messageObject))
            print('-1----')
            return str(self.messageObject)
        except Exception as get_email_object_e:
            raise get_email_object_e

    def click_links(self):
        """获取邮件正文内容"""
        msgBodyContents = []
        if self.messageObject.is_multipart():  # 判断邮件是否由多个部分构成
            print('多个部分构成')
            te = ''
            messageParts = self.messageObject.get_payload()  # 获取邮件附载部分
            print('oooooooooooooooooooooooo')
            print(type(messageParts[0]))
            import re

            match_group = re.match(
                r'.*?https://store.steampowered.com/account/newaccountverification(.*?)" style="border-radius: 2px; padding: 1px; display.*?">',
                str(messageParts[1]), re.M | re.I | re.S | re.IGNORECASE)
            base_url = 'https://store.steampowered.com/account/newaccountverification'
            base_url = base_url + str(match_group.group(1))
            print("-----base_url---" + base_url)
            with open('base_url.txt', 'w', encoding='utf-8') as base_url_f:
                base_url_f.write(base_url)
            with open('base_url.txt', 'r', encoding='utf-8') as base_url_f:
                base_url = base_url_f.read()
            base_url = base_url.replace('\n', '').replace('\t', '').strip()
            response = requests.get(base_url)
            system_log(self.userAdr + " 邮件 需点击 验证返回码：" + str(response.status_code))
            system_log(self.userAdr + " 邮件 需点击 的url ：" + response.url)
            system_log(self.userAdr + " 邮件 需点击 的邮件结果 ：" + response.text)
            self.parse_url = response.url
            self.parse_status = response.status_code

            print('ppppppppppppppppppppppppppppppppppppppppp')
            print(messageParts[1])
            print('0xxxxxxxxxxxxxxxxxxxxxxxxx')
            # for messagePart in messageParts:
            #     bodyContent = decodeBody(messagePart)
            #     print("---11" + bodyContent)
            #     te = te + str(bodyContent)
            #     if bodyContent:
            #         msgBodyContents.append(bodyContent)

            # print(''.join(msgBodyContents))
            print('-----------------------9999999999999999999' + te)
        else:
            print('不是 。。。多个部分构成')
            bodyContent = decodeBody(self.messageObject)
            if bodyContent:
                msgBodyContents.append(bodyContent)

    def get_reg_url(self):
        """
        获取url
        :return:
        """
        match_group = re.match(
            r'.*?https://store.steampowered.com/account/newaccountverification(.*?)" style="border-radius: 2px; padding: 1px; display.*?">',
            str(self.messageObject), re.M | re.I | re.S | re.IGNORECASE)
        base_url = 'https://store.steampowered.com/account/newaccountverification'
        base_url = base_url + str(match_group.group(1))
        base_url = base_url.replace('\n', '').replace('\t', '').strip()
        response = requests.get(base_url)
        system_log(self.userAdr + " 邮件 需点击 验证返回码：" + str(response.status_code))
        system_log(self.userAdr + " 邮件 需点击 的url ：" + response.url)
        system_log(self.userAdr + " 邮件 需点击 的邮件结果 ：" + response.text)
        print("-----base_url---" + base_url)
        # return base_url

    def get_date(self):
        try:
            msgDate = self.messageObject["date"]
            print("date" + msgDate)
        except Exception as get_date_e:
            raise get_date_e

    def get_senderAdr(self):
        """
        返回 发送者和源邮件地址
        :return:
        """
        try:
            senderContent = self.messageObject["From"]
            # parseaddr()函数返回的是一个元组(realname, emailAddress)
            senderRealName, senderAdr = parseaddr(senderContent)
            # 将加密的名称进行解码
            senderRealName = decodeMsgHeader(senderRealName)
            print(senderRealName)
            print(senderAdr)
            return senderRealName, senderAdr
        except Exception as get_senderAdr_e:
            raise get_senderAdr_e

    def parse_msgHeader(self):
        msgHeader = self.messageObject["Subject"]
        # 对头文件进行解码
        msgHeader = decodeMsgHeader(msgHeader)
        print('对头文件进行解码 :' + msgHeader)

    def get_main_content(self):
        """获取邮件正文内容"""
        msgBodyContents = []
        if self.messageObject.is_multipart():  # 判断邮件是否由多个部分构成
            messageParts = self.messageObject.get_payload()  # 获取邮件附载部分
            for messagePart in messageParts:
                bodyContent = decodeBody(messagePart)
                if bodyContent:
                    msgBodyContents.append(bodyContent)
        else:
            bodyContent = decodeBody(self.messageObject)
            if bodyContent:
                msgBodyContents.append(bodyContent)
        print('获取邮件正文内容')
        print(msgBodyContents)
        return msgBodyContents

    def get_messageAttachments(self):
        messageAttachments = []
        if self.messageObject.is_multipart():  # 判断邮件是否由多个部分构成
            messageParts = self.messageObject.get_payload()  # 获取邮件附载部分
            for messagePart in messageParts:
                name = messagePart.get_param("name")  # 名字存在，则表示此部分为附件
                if name:
                    fileName = decodeMsgHeader(name)  # 解码
                    messageAttachments.append(fileName)
        else:
            name = self.messageObject.get_param("name")
            if name:
                fileName = decodeMsgHeader(name)  # 解码
                messageAttachments.append(fileName)
        print('获取邮件附载部分')
        print(messageAttachments)

    def quit_pop3_service(self):
        """ 终止POP3服务"""
        self.pop3Server.quit()
