
import parser
import requests
from bs4 import BeautifulSoup

class req_functions:
    def get_products_dns(search: str):
        headers_dns = {
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
        }
        url = f'https://www.dns-shop.ru/search/?q={search}&utm_referrer'
        """     https://www.dns-shop.ru/search/?q=xiaomi+redmi"""
        print("Эталон       : https://www.dns-shop.ru/search/?q=xiaomi+redmi")
        print("Фактически   : " + url)
        session_dns = requests.session()  # Cоздаётся объект тип session
        session_dns.headers.update(headers_dns)
        rs_dns = session_dns.get(url)

        test = requests.get(url)
        print(test.content)

        """Траблы с запросом"""
        if (str(rs_dns).find("location.href=ipp.makeUrl") != -1):
            pass  # всё хорошо
        else:  # Надо перейти по ссылке
            url = "https://www.dns-shop.ru/search/?q=" + search + "&utm_referrer=&"
            try:
                rs_dns = session_dns.get(url)
                print(rs_dns)
            except:
                print("Снова гавно")

        # data_dns = rs_dns.json()#создание сессии и соединения в DNS
        """   r = requests.get(link)
          soup = BeautifulSoup(r.content, 'html.parser')
          """
        root_dns = BeautifulSoup(rs_dns.content, 'html.parser')
        print(root_dns.prettify())
        search_class = chr(92) + chr(34) + "n-catalog-product__main" + chr(92) + chr(34)
        tags_dns = root_dns.find_all("div", class_=search_class)

        products_dns = []
        for tag in tags_dns:
            products_dns.append(parser.products.product_dns(str(tag)))
            print(products_dns[len(products_dns) - 1].to_string())

        return products_dns

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
            items_ct.append(parser.products.product_citilink(str(tag)))
            items_ct[i].to_string()
            i += 1
            print(
                "____________________________________________________________________________________________________________________________________________________")
        return items_ct

    def get_products_eldorado(search: str):
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
            items_ct.append(parser.products.product_citilink(str(tag)))
            items_ct[i].to_string()
            i += 1
            print(
                "____________________________________________________________________________________________________________________________________________________")
        return items_ct
