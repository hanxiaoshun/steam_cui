import poplib
import random
from email.header import decode_header
from email.parser import Parser
from email.utils import parseaddr


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
                print("555555555555" + charset)
        print('999')
        print(content)
        print('7777')
        # if charset:
        #     textContent = content.decode(charset)

    return textContent


"""POP的服务器信息"""
popHost = "pop.126.com"
userAdr = "bufandaojia20886@126.com"
userPwd = "qiaotuanbixie"

""" 创建POP3对象，添加用户名和密码"""
pop3Server = poplib.POP3(popHost)
pop3Server.user(userAdr)
pop3Server.pass_(userPwd)

"""获取邮件数量和占用空间"""
messageCount, mailboxSize = pop3Server.stat()
print("邮件数量...start")
print(messageCount, mailboxSize)
print("邮件数量...end")
"""获取邮件请求返回状态码、每封邮件的字节大小(b'第几封邮件 此邮件字节大小')、"""
response, msgNumOctets, octets = pop3Server.list()

""" 获取任意一封邮件的邮件对象【第一封邮件的编号为1，而不是0】"""
# msgIndex = random.randint(1, messageCount)
# print(msgIndex)
# 获取第msgIndex封邮件的信息
response, msgLines, octets = pop3Server.retr(messageCount)
# msgLines中为该邮件的每行数据,先将内容连接成字符串，再转化为email.message.Message对象
msgLinesToStr = b"\r\n".join(msgLines).decode("utf8", "ignore")
messageObject = Parser().parsestr(msgLinesToStr)
import re

match_group = re.match(
    r'.*?https://store.steampowered.com/account/newaccountverification(.*?)" style="border-radius: 2px; padding: 1px; display.*?">',
    str(messageObject), re.M | re.I | re.S | re.IGNORECASE)
base_url = 'https://store.steampowered.com/account/newaccountverification'
base_url = base_url + str(match_group.group(1))
print("-----kkkkk---" + base_url)
import requests
response_a = requests.get(base_url)
print(response_a.status_code)
print(response_a.text)
print('---00-----')
print(type(str(messageObject)))

print("------------------------------999-------" + str(messageObject))

msgDate = messageObject["date"]
print("date" + msgDate)

senderContent = messageObject["From"]
# parseaddr()函数返回的是一个元组(realname, emailAddress)
senderRealName, senderAdr = parseaddr(senderContent)
# 将加密的名称进行解码
senderRealName = decodeMsgHeader(senderRealName)
print(senderRealName)
print(senderAdr)
print('对头文件进行解码')
msgHeader = messageObject["Subject"]
# 对头文件进行解码
msgHeader = decodeMsgHeader(msgHeader)
print('对头文件进行解码 :' + msgHeader)

"""获取邮件正文内容"""
msgBodyContents = []
if messageObject.is_multipart():  # 判断邮件是否由多个部分构成
    print('多个部分构成')
    te = ''
    messageParts = messageObject.get_payload()  # 获取邮件附载部分
    print('oooooooooooooooooooooooo')
    print(type(messageParts[0]))
    import re

    match_group = re.match(
        r'.*?https://store.steampowered.com/account/newaccountverification(.*?)" style="border-radius: 2px; padding: 1px; display.*?">',
        str(messageParts[1]), re.M | re.I | re.S | re.IGNORECASE)
    base_url = 'https://store.steampowered.com/account/newaccountverification'
    base_url = base_url + str(match_group.group(1))
    print("-----pp---" + base_url)
    print('ppppppppppppppppppppppppppppppppppppppppp')
    print(messageParts[1])
    print('0xxxxxxxxxxxxxxxxxxxxxxxxx')
    for messagePart in messageParts:
        bodyContent = decodeBody(messagePart)
        print("---11" + bodyContent)
        te = te + str(bodyContent)
        if bodyContent:
            msgBodyContents.append(bodyContent)

    # print(''.join(msgBodyContents))
    print('-----------------------9999999999999999999' + te)
else:
    print('不是 。。。多个部分构成')
    bodyContent = decodeBody(messageObject)
    if bodyContent:
        msgBodyContents.append(bodyContent)
print('获取邮件正文内容')
print(msgBodyContents)
print('获取邮件正文内容')
messageAttachments = []
if messageObject.is_multipart():  # 判断邮件是否由多个部分构成
    messageParts = messageObject.get_payload()  # 获取邮件附载部分
    for messagePart in messageParts:
        name = messagePart.get_param("name")  # 名字存在，则表示此部分为附件
        if name:
            fileName = decodeMsgHeader(name)  # 解码
            messageAttachments.append(fileName)
else:
    name = messageObject.get_param("name")
    if name:
        fileName = decodeMsgHeader(name)  # 解码
        messageAttachments.append(fileName)
print('获取邮件附载部分')
print(messageAttachments)

""" 终止POP3服务"""
pop3Server.quit()
import requests
response_a = requests.get(base_url)
print(response_a.status_code)
print(response_a.text)
print('---00-----')
print(type(str(messageObject)))