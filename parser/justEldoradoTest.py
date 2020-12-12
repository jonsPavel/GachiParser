from bs4 import BeautifulSoup
import json
import requests


class Product_eldorado:
    name = "eldorado"
    def __init__(self,js__subcategory_product_item):
        soup = BeautifulSoup(js__subcategory_product_item, 'html.parser')
        prettify=soup.prettify()
        """Вытаскивание словаря с аттрибутами 'price' и 'shortName'    """
        image_link=soup.find('div',class_='AkWZIIC').find('img',attrs={'srcset':True})['src']

        attributes_list_tag = soup.find('ul',class_='_1hV310P').contents # характеристики
        attributes_list=[]
        for i in attributes_list_tag:
            attributes_list.append(i.text)
        name_link = soup.find('div',class_='_2fFxlhy') # название, ссылка
        name=name_link.contents[0].text
        link='https://www.eldorado.ru/'+name_link.contents[0].attrs['href']
        price=soup.find('span',class_='wcf6ic-1 sc-1nnsxdl-1 gILnXT').text

        flag_d = False
        i = 0

        # description=description.strip(" ")

        self.link = link
        self.image =image_link
        self.name = name
        self.price = price
        pass

    def to_string(self):
        print("Название товара:\t\t\t"+str(self.name))
        print("Цена товара:\t\t\t\t"+str(self.price))
        print("Ссылка на картинку :\t\t"+str(self.image))
        print("Ссылка на продукт товара:\t"+str(self.link))


class get_eldorado:
    @staticmethod
    def get_products_eldorado(search: str):
        headers_eldorado = {  # Заголовки
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
        }
        url = f'https://www.eldorado.ru/search/catalog.php?q={search}'
        session_eldorado = requests.session()               # Cоздаётся объект тип session
        session_eldorado.headers.update(headers_eldorado)   # загружаются заголовки
        response_eldorado = session_eldorado.get(url)             # делаем запрос


        bs_eldorado = BeautifulSoup(response_eldorado.text, 'html.parser')
        items_eldorado = []
        tags_eldorado = bs_eldorado.find_all('li',attrs={'class': True, 'data-dy': True, 'data-id': True,
                                                    'data-product-index': True})  # поиск по предложениям
        i = 0
        for tag in tags_eldorado:  # создание объектов продукта
            items_eldorado.append(Product_eldorado(str(tag)))
            items_eldorado[i].to_string()
            i += 1
            print(
                "____________________________________________________________________________________________________________________________________________________")
        return items_eldorado

if __name__=="__main__":

    testEldorado = get_eldorado()
    print("Введите ваш запрос:")
    y_req=input().replace(" ","+")
    items_eldorado=testEldorado.get_products_eldorado(y_req)
    for i in items_eldorado:
        i.to_string()
        print(
            "____________________________________________________________________________________________________________________________________________________")
