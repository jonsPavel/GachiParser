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

class product_citilink:
    def __init__(self,js__subcategory_product_item):

        soup = BeautifulSoup(js__subcategory_product_item, 'html.parser')

        """Вытаскивание словаря с аттрибутами 'price' и 'shortName'    """
        attributes_dictionary = soup.find('div').attrs
        data_params = attributes_dictionary["data-params"]
        decoded = json.loads(data_params)

        image_attr = soup.find("img").attrs

        link_attr = soup.find("a").attrs

        description = str(soup.find("p", class_="short_description").get_text())
        flag_d = False
        i = 0

        for w in description:
            if flag_d and ord(w) != 32:
                description = str(description[i:len(description)-1])
                break
            if w == ";":
                flag_d = True
            i += 1
        # description=description.strip(" ")

        self.link = link_attr["href"]
        self.image =image_attr["data-src"]
        self.name = decoded["shortName"]
        self.price = decoded["price"]
        self.description = description


        pass

    def to_string(self):
        print("Название товара:\t\t\t"+str(self.name))
        print("Цена товара:\t\t\t\t"+str(self.price))
        print("Ссылка на картинку :\t\t"+str(self.image))
        print("Ссылка на продукт товара:\t"+str(self.link))
        print("Описание товара:\t"+str(self.description.strip(' ')))


class product_eldorado:
    def __init__(self,js__subcategory_product_item):

        soup = BeautifulSoup(js__subcategory_product_item, 'html.parser')

        """Вытаскивание словаря с аттрибутами 'price' и 'shortName'    """
        attributes_dictionary = soup.find('div').attrs
        data_params = attributes_dictionary["data-params"]
        decoded = json.loads(data_params)

        image_attr = soup.find("img").attrs

        link_attr = soup.find("a").attrs

        description = str(soup.find("p", class_="short_description").get_text())
        flag_d = False
        i = 0

        for w in description:
            if flag_d and ord(w) != 32:
                description = str(description[i:len(description)-1])
                break
            if w == ";":
                flag_d = True
            i += 1
        # description=description.strip(" ")

        self.link = link_attr["href"]
        self.image =image_attr["data-src"]
        self.name = decoded["shortName"]
        self.price = decoded["price"]
        self.description = description


        pass

    def to_string(self):
        print("Название товара:\t\t\t"+str(self.name))
        print("Цена товара:\t\t\t\t"+str(self.price))
        print("Ссылка на картинку :\t\t"+str(self.image))
        print("Ссылка на продукт товара:\t"+str(self.link))
        print("Описание товара:\t"+str(self.description.strip(' ')))

