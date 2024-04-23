import requests

URL = 'https://api.ipify.org'

res = requests.get(URL)
#print(res.text)
print(res.json())
ip_dict = res.json()

ip = res.json()
