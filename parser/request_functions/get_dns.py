import requests
from bs4 import BeautifulSoup


class get_dns:
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



