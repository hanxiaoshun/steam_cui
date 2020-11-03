
import re
test = 'https://mail.126.com/js6/main.jsp?sid=sAapoSrrVNLcNdvSrPrroOyMedrHAtGe&df=mail126_letter#module=welcome.WelcomeModule%7C%7B%7D '

match_group = re.match(r'.*?sid=(.*?)&df=mail.*?', test, re.M | re.I | re.S | re.IGNORECASE)
sid = match_group.group(1)
print('sid : ', sid)

# match_group = re.match(r'.*?id="(.*?)" role="link"', html,
#                        re.M | re.I | re.S | re.IGNORECASE)
# print(match_group.group(1))