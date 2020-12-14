# from parser.products_selection.eldorado_selection import Product_eldorado
from parser.products_selection import eldorado_selection
import requests
from bs4 import BeautifulSoup

class get_eldorado:

    @staticmethod
    def get_products_eldorado(self,search: str):
        headers_eldorado = {  # Заголовки
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
        }
        url = f'https://www.eldorado.ru/search/catalog.php?q={search}'
        # session_eldorado = requests.session()               # Cоздаётся объект тип session
        # session_eldorado.headers.update(headers_eldorado)   # загружаются заголовки
        # rs_eldorado = session_eldorado.get(url)             # делаем запрос
        test = requests.get(url)
        print(test.content)
        # data_eldorado = rs_eldorado.json()                  # переводим в json
        # print(rs_eldorado)

        root_eldorado = BeautifulSoup(test.content['html'], 'html.parser')
        items_eldorado = []
        tags_ct = root_eldorado.find_all(class_="sc-1w9a1pg-0 sc-19ibhqc-0 gUmybO")  # поиск по предложениям
        i = 0
        for tag in tags_ct:  # создание объектов продукта
            items_eldorado.append(eldorado_selection.Product_eldorado(str(tag)))
            items_eldorado[i].to_string()
            i += 1
            print(
                "____________________________________________________________________________________________________________________________________________________")
        return items_eldorado

