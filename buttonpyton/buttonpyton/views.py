from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
import sys
import datetime
from testSelenium import Product_eKatalog


def button(request):
    return render(request,'home.html')

def output(request):
    data = requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request, 'home.html', {'data':data})

def external(request):
    y_req = []
    y_req = Product_eKatalog.fun(request)
    for i in y_req:
        max = -1;
        min = -1;
        quantyty = 1;
        for j in i.data_about_magazines:
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

    return render(request,'home.html',context={"langs": y_req})
