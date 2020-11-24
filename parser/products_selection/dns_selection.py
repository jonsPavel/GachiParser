from bs4 import BeautifulSoup
import json


class product_dns:

    def __init__(self,n_catalog_product__main):

        soup = BeautifulSoup(n_catalog_product__main, 'html.parser')
        name_class = chr(92)+chr(34)+"ui-link"+chr(92)+chr(34)
        self.name = str(soup.find("a",class_=name_class).text)

        price_class=chr(92)+chr(34)+"product-min-price__current"+chr(92)+chr(34)
        # self.name = str(soup.find("div").find("div").find(class__="product-info__title-link "))
        self.price = str(soup.find("div",class_=price_class))

        pass

    def to_string(self):
        print(self.name)
        print(self.price)
