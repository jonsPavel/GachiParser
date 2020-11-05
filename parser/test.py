import requests
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')


y_req=input("Введите ваш запрос:\t")
y_req=str(y_req.replace(' ','+'))
url = f'https://www.dns-shop.ru/search/?q={y_req}'

response = driver.get(url)
# print(response)
# session = requests.Session()
# session.allow_redirects=True
# session.max_redirects = 3
# session.cookies=''
# response =session.get(url)
# response = requests.get(url)

bs=BeautifulSoup(str(response), 'html.parser')
# print(response.status_code)
print(bs.prettify())