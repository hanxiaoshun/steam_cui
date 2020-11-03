import requests
import json


def steam_title():
    """
    获得打码所需的 sitekey
    :return:
    """
    # main_header = {
    #     'User-Agent': self.user_agent,
    #     'Origin': self.origin,
    #     'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': self.language,
    #     'Connection': 'keep-alive',
    #     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    #     'Host': 'store.steampowered.com',
    #     'Referer': self.first_referer
    # }
    # post_data = {'user': '15847433555',
    #              'pass': 'cuizhi8899',
    #              'token': '4eb42929b6e6b61f4ab7c7dbfa011e93',
    #              'act': 'mail',
    #              'type': 'read',
    #              'email': 'mdqnqi@126.com',
    #              'pwd': 'jqy8o8laf',
    #              'title': 'Steam'}
    # '&token=4eb42929b6e6b61f4ab7c7dbfa011e93'
    url = 'http://ocr.xinby.cn/api.php?user=15847433555&pass=cuizhi8899&act=mail&type=read&email=mdqnqi@126.com&pwd=jqy8o8laf&title=Steam&format=html'
    response = requests.get(url)  # 传递cookie

    import re
    print(response.text)
    match_group = re.match(
        r'.*?https%3A%2F%2Fstore.steampowered.com%2Faccount%2Fnewaccountverification%3F(.*?)&amp;keyfrom=jumper.in&amp;c=TRUE&amp;j=1&amp.*?">',
        str(response.text), re.M | re.I | re.S | re.IGNORECASE)
    base_url = 'https://store.steampowered.com/account/newaccountverification?'
    print(match_group.group(1))
    stoken_creationid = str(match_group.group(1)).replace('%3D', '=').replace('%26', '&')
    base_url = base_url + stoken_creationid
    print('base_url :::', base_url)
    res = requests.get(base_url)
    print(res.text)
    # self.cookies.set('cookie-name', 'cookie-value', path='/', domain='.abc.com')  # 保存更新cookie
    # self.session.cookies.update(response.cookies)
    # # {"gid": "2498864890707537149", "type": 2, "sitekey": "6LerFqAUAAAAABMeByEoQX9u10KRObjwHf66-eya"}
    # json_data = json.loads(response.text)
    # self.captchagid_gid = json_data['gid']
    # self.type = json_data['type']
    # self.sitekey = json_data['sitekey']


if __name__ == '__main__':
    steam_title()
