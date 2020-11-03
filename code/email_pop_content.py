import re

get_email_object = """
以及在未来能够安全的找回您的帐户。

感谢您协助我们确认您帐户的安全性。

- Steam 团队


*若您最近并未使用本电子邮件地址新建 Steam
帐户，您可以放心地忽略此邮件。

View this message on the web:
<https://store.steampowered.com/email/AccountCreationEmailVerification?sparams=eJxdkNFqxCAQRf8lD30qG5040Sws7T_0NRDMOOmGbjQY7VJK_72mpFD6NM69d86on9XNZk9Xjulj5epcieqxWmNwmZK3y668JLZLUbe8riEmXux8K_LRPm-7vYY7R3YnCnvyCG3sU05UshK1bkECqOK-c5ynmWyagx9y3FnXlNbt3Nd9vaUQ-fSf2deWKGSf-trz_Tj_5TyVuTf2F0NGOdGWglPnYFRo5MQaYULdtiyNbCRhRxo0KocCRwnCGNcKcNCRktoIMcpyWbYSbGeVKWNTQdqS4emBIv8snN3FYIEpJZq2EwiIAE15nc_LsNhE19m_Dr9_Jaqvb0OodYc>


--np5e0896e827366
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: 7bit

<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title></title>
	</head>
<style media="all" type="text/css">
	td, p, h1, h3, a {
		font-family: Helvetica, Arial, sans-serif;
	}
</style>
<body bgcolor="" LINK="#6d93b8" ALINK="#9DB7D0" VLINK="#6d93b8" TEXT="#d7d7d7" style="font-family: Helvetica, Arial, sans-serif; font-size: 14px; color: #d7d7d7;">
	<center style="color: #000000; font-size: 11px; margin-bottom: 4px;">查看此消息时遇到问题？ <a href="https://store.steampowered.com/email/AccountCreationEmailVerification?sparams=eJxdkNFqxCAQRf8lD30qG5040Sws7T_0NRDMOOmGbjQY7VJK_72mpFD6NM69d86on9XNZk9Xjulj5epcieqxWmNwmZK3y668JLZLUbe8riEmXux8K_LRPm-7vYY7R3YnCnvyCG3sU05UshK1bkECqOK-c5ynmWyagx9y3FnXlNbt3Nd9vaUQ-fSf2deWKGSf-trz_Tj_5TyVuTf2F0NGOdGWglPnYFRo5MQaYULdtiyNbCRhRxo0KocCRwnCGNcKcNCRktoIMcpyWbYSbGeVKWNTQdqS4emBIv8snN3FYIEpJZq2EwiIAE15nc_LsNhE19m_Dr9_Jaqvb0OodYc">点击此处</a></center>
<table style="width: 538px; background-color: #393836;" align="center" cellspacing="0" cellpadding="0">
	<tr>
		<td style=" height: 65px; background-color: #000000; border-bottom: 1px solid #4d4b48;">
			<img src="https://steamstore-a.akamaihd.net/public/shared/images/header/globalheader_logo.png" height="44" border="0" >
		</td>
	</tr>
	<tr>
		<td bgcolor="#17212e">
			<table width="470" border="0" align="center" cellpadding="0" cellspacing="0" style="padding-left: 5px; padding-right: 5px; padding-bottom: 10px;">

				<tr>
					<td style="padding-top: 32px; font-size: 24px; color: #66c0f4; font-family: Arial, Helvetica, sans-serif; font-weight: bold;">
						您好：					</td>
				</tr>
				<tr>
					<td style="padding-top: 10px; padding-bottom: 30px; font-size: 24px; color: #66c0f4; font-family: Arial, Helvetica, sans-serif;">
						即将完成！					</td>
				</tr>

				<tr>
					<td style="font-size: 14px; padding: 16px; background-color:#121a25; color:#FFF" >
						验证您的电子邮件地址来完成您 Steam 帐户的创建。					</td>
				</tr>

				<tr>
					<td style="padding: 16px; background-color:#121a25;">
						<table cellpadding="0" cellspacing="0" border="0" align="center">
							<tr>
																	<td style="background: #799905;height: 32px;text-align: center" align="center" >
										<a href="https://store.steampowered.com/account/newaccountverification?stoken=8c84d068c85f9d2b4581fe752f5766e18131c59c72754d505b12088d602d29c417800b1762ea12a9a4866efd06ad60ef&creationid=8513144036905255223" style="border-radius: 2px; padding: 1px; display: block; text-decoration: none; color: #D2E885; background: #799905; background: -webkit-linear-gradient( top, #799905 5%, #536904 95%);
	background: linear-gradient( to bottom, #799905 5%, #536904 95%);
text-shadow: -1px -1px 0px rgba( 0, 0, 0, 0.1 );" >
										<span style="border-radius: 2px; display: block; padding: 0; font-size: 20px; line-height: 32px; ">
											&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;创建我的帐户&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
										</span>
										</a>
									</td>
															</tr>
						</table>
					</td>
				</tr>

				<tr>
					<td style="padding-top: 16px; font-size: 12px; line-height: 17px; color: #6d7880;">
						您需要向 Steam 提供一个验证过的电子邮件地址来使用 Steam 的完整功能，诸如 Steam 令牌、Steam 社区市场、Steam 交易 - 以及在未来能够安全的找回您的帐户。					</td>
				</tr>

				<tr>
					<td style="padding-top: 16px; font-size: 12px; line-height: 17px; color: #6d7880;" >
						感谢您协助我们确认您帐户的安全性。					</td>
				</tr>

				<tr>
					<td style="font-size: 12px; color: #6d7880; padding-top: 16px; ">
						- Steam 团队					</td>
				</tr>

				<tr>
					<td style="padding-top: 40px; font-size: 12px; line-height: 17px; color: #6d7880; ">
						*若您最近并未使用本电子邮件地址新建 Steam 帐户，您可以放心地忽略此邮件。					</td>
				</tr>

			</table>
		</td>
	</tr>
	<tr style="background-color: #000000;">
		<td style="padding: 12px 24px;">
			<table cellpadding="0" cellspacing="0">
				<tr>
					<td width="92">
						<img src="https://steamstore-a.akamaihd.net/public/images/logo_valve_footer.jpg" width="92" height="26" alt="Valve&reg;">
					</td>
					<td style=" font-size: 11px; color: #595959; padding-left: 12px;">
						© Valve Corporation<br>PO Box 1688 Bellevue, WA 98009<br>
						保留所有权利。所有商标均为其在美国及其它国家/地区的各自持有者所有。					</td>
				</tr>
			</table>
		</td>
	</tr>
</table>
	<center style="color: #000000; font-size: 11px; margin-bottom: 4px;">查看此消息时遇到问题？ <a href="https://store.steampowered.com/email/AccountCreationEmailVerification?sparams=eJxdkNFqxCAQRf8lD30qG5040Sws7T_0NRDMOOmGbjQY7VJK_72mpFD6NM69d86on9XNZk9Xjulj5epcieqxWmNwmZK3y668JLZLUbe8riEmXux8K_LRPm-7vYY7R3YnCnvyCG3sU05UshK1bkECqOK-c5ynmWyagx9y3FnXlNbt3Nd9vaUQ-fSf2deWKGSf-trz_Tj_5TyVuTf2F0NGOdGWglPnYFRo5MQaYULdtiyNbCRhRxo0KocCRwnCGNcKcNCRktoIMcpyWbYSbGeVKWNTQdqS4emBIv8snN3FYIEpJZq2EwiIAE15nc_LsNhE19m_Dr9_Jaqvb0OodYc">点击此处</a></center>

</body>
</html>
"""
match_group = re.match(
    r'.*?https://store.steampowered.com/account/newaccountverification(.*?)" style="border-radius: 2px; padding: 1px; display.*?">',
    str(get_email_object), re.M | re.I | re.S | re.IGNORECASE)
base_url = 'https://store.steampowered.com/account/newaccountverification'
base_url = base_url + str(match_group.group(1))
print(base_url)