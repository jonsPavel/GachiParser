import requests
from bs4 import BeautifulSoup
import json
import re
import json
class get_citilink:
    """СИГНАТУРА:"""

    """ ВВОД:        форматированная строка поиска вида xiaomi+redmi"""
    """ ВОЗВРАТ:        СПИСОК ТОВАРОВ"""

    def get_products_citilink(self,search: str):
        headers_citilink = {  # Заголовки
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
        }

        url = f'https://www.citilink.ru/search/?text={search}'
        session_citilink = requests.session()  # Cоздаётся объект тип session
        session_citilink.headers.update(headers_citilink)  # загружаются заголовки
        rs_citilink = session_citilink.get(url)  # делаем запрос
        data_citilink = rs_citilink.json()  # переводим в json

        root_ct = BeautifulSoup(data_citilink['html'], 'html.parser')
        root_ct_prettify=root_ct.prettify()
        items_ct = []
        tags_ct = root_ct.find_all('div', attrs={'class': True, 'data-params': True, 'data-product-id': True,
                                                    'data-url': True})
        i = 0
        for tag in tags_ct:  # создание объектов продукта

            items_ct.append(product_citilink(str(tag)))
            # items_ct[i].to_string()
            i += 1
            # print(
            #     "____________________________________________________________________________________________________________________________________________________")
        return items_ct




class product_citilink:
    def __init__(self,html):
        self.html_data = html
        self.soup = BeautifulSoup(html, 'html.parser')
        attributes_dictionary = self.soup.find('div').attrs
        data_params = attributes_dictionary["data-params"]

        decoded = json.loads(data_params)

        image_attr = self.soup.find("img").attrs

        link_attr = self.soup.find("a").attrs

        self.link = "https://www.citilink.ru/"+link_attr["href"]
        self.image =image_attr["src"]
        self.name = decoded["shortName"]
        self.price = decoded["price"]
        flag_d = False

    def to_string(self):
        print("Название товара:\t\t\t"+str(self.name))
        print("Цена товара:\t\t\t\t"+str(self.price))
        print("Ссылка на картинку :\t\t"+str(self.image))
        print("Ссылка на продукт товара:\t"+str(self.link))


if __name__ == '__main__':
    ps = get_citilink()
    print("Введите ваш запрос:")
    y_req=input().replace(" ","+")
    items_ct = ps.get_products_citilink(y_req)


    def sortByPrice(product_citilink ):
        return int(product_citilink.price)
    items_ct.sort(key=sortByPrice,reverse=True)

    for i in items_ct:
        i.to_string()
        print(
            "____________________________________________________________________________________________________________________________________________________")

    # print(f'Search {y_req!r}...')
    #
    # print(len(items_ct))
    # print(f'  Result ({len(items_ct)}):')
