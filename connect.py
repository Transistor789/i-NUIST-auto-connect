import json
import requests

#======================================#
username = "15388888888"  # 手机号
password = "666666"  # 密码
channel = "3"  # 移动：2  电信：3 联通：4
#======================================#

ip = requests.get('http://10.255.255.34/api/v1/ip').json()["data"]
data_raw = {
    'username': username,
    'password': password,
    'channel': channel,
    'ifautologin': '0',
    'pagesign': 'secondauth',
    'usripadd': ip
}
data = json.dumps(data_raw, separators=(',', ':'))
response = requests.post('http://10.255.255.34/api/v1/login', data)
print(response.text)
