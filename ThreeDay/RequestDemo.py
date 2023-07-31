import requests

x = requests.get('https://w3school.com.cn/python/demopage.htm')

print(x.text)
