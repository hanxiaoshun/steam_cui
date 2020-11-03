import requests
res = requests.get('https://store.steampowered.com/account/newaccountverification?')
print(res.status_code)
res = requests.get('https://store.steampowered.com/account/newaccountverification?stoken=1109e2658a9948cb41a39402660232c3dfc0a94e60dba12413fed64bc72dd3d3e8fae03f1746e6e2a1074a06b6eecafe&creationid=1156594058276489589')
print(res.status_code)