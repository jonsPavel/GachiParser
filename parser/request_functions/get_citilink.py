import requests
from bs4 import BeautifulSoup
from parser.products_selection.citilink_selection import product_citilink

class get_citilink:
    """СИГНАТУРА:"""

    """ ВВОД:        форматированная строка поиска вида xiaomi+redmi"""
    """ ВОЗВРАТ:        СПИСОК ТОВАРОВ"""


    def get_products_citilink(search: str):
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
        items_ct = []
        tags_ct = root_ct.find_all(class_="js--subcategory-product-item")  # поиск по предложениям
        i = 0
        for tag in tags_ct:  # создание объектов продукта
            items_ct.append(product_citilink(str(tag)))
            items_ct[i].to_string()
            i += 1
            print(
                "____________________________________________________________________________________________________________________________________________________")
        return items_ct

