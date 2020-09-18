import requests
from bs4 import BeautifulSoup


# https://rasm.io/person/54017742/%D9%85%D9%87%D8%AF%DB%8C%20%D9%81%D8%B6%D9%84%DB%8C/
# 54017742 = id

url = 'https://rasm.io/person/10613889/%D8%B1%D8%B6%D8%A7%20%D8%AA%D8%B1%DA%A9%D8%AA%D8%A7%D8%B2/'
# response = requests.get(url=url, headers={'Connection': 'keep-alive', 'Accept-Encoding': 'gzip, deflate, br',
#                                           'Cookie': '_ga=GA1.2.1841057450.1592754364; _hp2_id.2248261963=%7B%22userId%22%3A%228409660356385405%22%2C%22pageviewId%22%3A%227483135379196493%22%2C%22sessionId%22%3A%228600140425505290%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; pushNotification-shownCount-6822=0; tlc=true; _gid=GA1.2.714763522.1598732689',
#                                           'Upgrade-Insecure-Requests': '1'})
response = requests.post(url=url)
x = response

soup = BeautifulSoup(open(url), "html.parser")
z = soup

# soup = BeautifulSoup(base_page.text, "html.parser")  # Parsing to html content
# print(soup)
