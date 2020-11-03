#!/usr/bin/python3
# coding: utf-8

import poplib
from email.header import decode_header
from email.parser import Parser
from email.utils import parseaddr


def print_msg(msg, indent=0):
    if indent == 0:
        for header in ["From", "To", "Subject", "Date"]:
            value = msg[header]
            if value:
                value = decode_str(value)
            print("%s%s: %s" % (" " * indent, header, value))
    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print("%spart %s" % (" " * indent, n))
            print_msg(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == "text/plain" or content_type == "text/html":
            content = msg.get_payload(decode=True)
            charset = get_charset(msg)
            if charset:
                content = content.decode(charset)
            print("%sText: %s" % (" " * indent, content))
        else:
            print("%sAttachment: %s" % (" " * indent, content_type))


def decode_str(s):
    l = decode_header(s)
    value, charset = l[0]
    if charset:
        value = value.decode(charset)

    if len(l) == 2:
        value_tmp = l[1][0]
        value = value + value_tmp.decode(charset)
    return value


def get_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get("Content-type", "").lower()
        pos = content_type.find("charset=")
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


from_email = "mdqnqi@126.com"
from_email_pwd = "jqy8o8laf"
pop_server = "pop.126.com"
server = poplib.POP3_SSL(pop3_server,port=995)
# server = poplib.POP3(pop_server)
server.set_debuglevel(1)
print(server.getwelcome().decode("utf-8"))

server.user(from_email)
server.pass_(from_email_pwd)

print("Messages: %s Size: %s" % (server.stat()))


"""{
'code':'S_OK',
'var':{
'from':['Steam <noreply@steampowered.com>'],
'to':['mdqnqi@126.com'],
'replyTo':['noreply@steampowered.com'],
'flags':{
},
'requestReadReceipt':false,
'isManualDisposition':true,
'subject':'新 Steam 帐户电子邮件验证',
'sentDate':new Date(2019,10,29,0,39,0),
'priority':3,
'headerRaw':'Received: from smtp-01-tuk1.steampowered.com (unknown [208.64.202.37])\r\n\tby mx10 (Coremail) with SMTP id KMmowAB3lz8j+N9dxKWlAg--.30382S3;\r\n\tFri, 29 Nov 2019 00:39:01 +0800 (CST)\r\nDKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/relaxed;\r\n\td=steampowered.com; s=smtp; h=Date:Message-Id:Content-Type:Subject:\r\n\tMIME-Version:Reply-To:From:To:Sender:Cc:Content-Transfer-Encoding:Content-ID:\r\n\tContent-Description:Resent-Date:Resent-From:Resent-Sender:Resent-To:Resent-Cc\r\n\t:Resent-Message-ID:In-Reply-To:References:List-Id:List-Help:List-Unsubscribe:\r\n\tList-Subscribe:List-Post:List-Owner:List-Archive;\r\n\tbh=f/zzQ6d6E1LDEDGCctfaWNB9CA9Mx4R5uJ/fB00CLsE=; b=KL8GgqChbYq3OSsS3k2+UEjPeZ\r\n\tNA1aUFE2ivbfcA+9Ok01W1LsXDnC25Zd5Cej9Qt3HBzWeQQ7BUTgRjUC/u3frAUiohK0O9bMQhKCX\r\n\teMzeg+j6UmYL6nSyJvNLGF6hh2dqf09fKgQwayQT/ed34j1YAgTszxfMF+HNNUUfS0Mc=;\r\nReceived: from [208.64.200.161] (helo=valvesoftware.com)\r\n\tby smtp-01-tuk1.steampowered.com with smtp (Exim 4.90_1)\r\n\t(envelope-from <noreply@steampowered.com>)\r\n\tid 1iaMom-00025M-5e\r\n\tfor mdqnqi@126.com; Thu, 28 Nov 2019 08:39:00 -0800\r\nTo: mdqnqi@126.com\r\nFrom: "Steam" <noreply@steampowered.com>\r\nReply-To: <noreply@steampowered.com>\r\nErrors-To: <noreply@steampowered.com>\r\nX-Steam-Message-Type: CAccountCreationEmailVerification\r\nMIME-Version: 1.0\r\nSubject: =?UTF-8?B?5pawIFN0ZWFtIOW4kOaIt+eUteWtkOmCruS7tumqjOivgQ==?=\r\nContent-Type: multipart/alternative;\r\n boundary="np5ddff82422a00"\r\nMessage-Id: <E1iaMom-00025M-5e@smtp-01-tuk1.steampowered.com>\r\nDate: Thu, 28 Nov 2019 08:39:00 -0800\r\nX-CM-TRANSID:KMmowAB3lz8j+N9dxKWlAg--.30382S3\r\nAuthentication-Results: mx10; spf=pass smtp.mail=noreply@steampowered.\r\n\tcom; dkim=pass header.i=@steampowered.com\r\nX-Coremail-Antispam: 1Uf129KBjDUn29KB7ZKAUJUUU88529EdanIXcx71UUUUU7v73\r\n\tVFW2AGmfu7bjvjm3AaLaJ3UbIYCTnIWIevJa73UjIFyTuYvjxU6znmUUUUU\r\n',
'headers':{
'Reply-To':['noreply@steampowered.com']},
'antispamInfo':{
'RulesType':'',
'GuestSender':null},
'html':{
'id':'2',
'contentType':'text/html',
'contentLength':5274,
'contentOffset':3261,
'estimateSize':5274},
'text':{
'id':'1',
'contentType':'text/plain',
'contentLength':1176,
'contentOffset':1989,
'estimateSize':1176},
'attachments':[]}}"""
resp, mails, octets = server.list()
index = len(mails)
resp, lines, octets = server.retr(index)
msg_content = b"\r\n".join(lines).decode("utf-8")

msg = Parser().parsestr(msg_content)
print_msg(msg)
server.quit()
