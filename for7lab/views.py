from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
import sys
import datetime
from testSelenium import Product_eKatalog
from selenium import webdriver
from bs4 import BeautifulSoup
import json

chromedriver = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
#browser.get('https://www.e-katalog.ru/ek-list.php?search_=xiaomi+redmi+note+7')
#print(123)

def button(request):
    return render(request,'home.html')

def backet(request):
    return render(request,'bascket.html')

def external(request):
    y_req = []
    y_req = Product_eKatalog.fun(request,browser)
    number = 1
    for i in y_req:
        max = -1;
        min = -1;
        quantyty = 1;
        d1 = {}
        d2 = {}
        d3 = {}
        for j in i.data_about_magazines:
            d1[quantyty]=j.price
            d2[quantyty]=j.name
            d3[quantyty]=j.link
            if min == 0:
                min = j.price
            if min > j.price:
                min = j.price
            if max < j.price:
                max = j.price
            quantyty+=1

        i.min = min
        i.max = max
        i.quantyty = quantyty
        i.number = number
        i.d1 = json.dumps(d1)
        i.d2 = json.dumps(d2)
        i.d3 = json.dumps(d3)
        number= number+1
        #обработка пустой выборки + если у товара нет магазина - вывести нет в продаже
    return render(request,'index.html',context={"langs": y_req})
