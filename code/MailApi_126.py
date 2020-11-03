import requests
import json
import re
import logging


def email_126(user, password, email_addres, email_pwd, email_title, act='mail', type='read', format='html'):
    """
    :param user:  魔云账户
    :param password: 魔云账户密码
    :param email_addres: 126 邮箱地址
    :param email_pwd: 邮箱密码
    :param email_title: 邮件标题
    :param act: 获取邮箱内容
    :param type: 读取文件
    :param format: 返回格式为HTML类型
    :return:
    """
    # url = 'http://ocr.xinby.cn/api.php?user=15847433555&pass=cuizhi8899&act=mail&type=read&email=mdqnqi@126.com&pwd=jqy8o8laf&title=Steam&format=html'
    url = 'http://ocr.xinby.cn/api.php?' \
          + 'user=' + user \
          + '&pass=' + password \
          + '&act=mail&type=read' \
          + '&email=' + email_address \
          + '&pwd=' + email_pwd \
          + '&title=' + email_title \
          + '&format=html'
    logging.info("\n -- url --" + url)
    response = requests.get(url)  # 传递cookie
    print(response.text)
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
    # if '即将完成' in res.text:
    #     return
    # self.cookies.set('cookie-name', 'cookie-value', path='/', domain='.abc.com')  # 保存更新cookie
    # self.session.cookies.update(response.cookies)
    # # {"gid": "2498864890707537149", "type": 2, "sitekey": "6LerFqAUAAAAABMeByEoQX9u10KRObjwHf66-eya"}
    # json_data = json.loads(response.text)
    # self.captchagid_gid = json_data['gid']
    # self.type = json_data['type']
    # self.sitekey = json_data['sitekey']


if __name__ == '__main__':
    user = '15847433555'
    password = 'cuizhi8899'
    act = 'mail'
    type = 'read'
    email_address = 'mdqnqi@126.com'
    email_pwd = 'jqy8o8laf'
    email_title = 'Steam'
    format = 'html'
    email_126(user, password, email_addres, email_pwd, email_title, act='mail', type='read', format='html')
