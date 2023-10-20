import requests
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/IPhone'
text=requests.get(url).text.encode('utf-8').decode('ascii', 'ignore')
# print(text)
soup= BeautifulSoup(text, 'lxml')
table=soup.find('table', {'class':'wikitable'} )
print((table))
# rows=table.find_all('tr')
# print(rows)

# for row in rows:
#     data=row.find_all(['th', 'td'])
#     try:
#      print(data[1:].a.text)
#     except:
#      pass