import requests

url='https://pypi.org/project/requests/'
res=requests.get(url)
print(res)