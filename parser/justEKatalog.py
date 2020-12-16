import requests
from bs4 import BeautifulSoup
import json
import lxml
import datetime
class get_eKatalog:
    """СИГНАТУРА:"""

    """ ВВОД:        форматированная строка поиска вида xiaomi+redmi"""
    """ ВОЗВРАТ:        СПИСОК ТОВАРОВ"""

    def get_products_eKatalog(self,search: str):
        headers_eKatalog = {  # Заголовки
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
        }

        url = f'https://www.e-katalog.ru/ek-list.php?search_={search}'
        session_eKatalog = requests.session()  # Cоздаётся объект тип session
        session_eKatalog.headers.update(headers_eKatalog)  # загружаются заголовки
        rs_eKatalog = session_eKatalog.get(url)  # делаем запрос
        # data_eKatalog = rs_eKatalog.json()  # переводим в json

        # root_ct = BeautifulSoup(str(rs_eKatalog), 'html.parser')
        root_ct = BeautifulSoup(str(rs_eKatalog.content), 'lxml')

        now=datetime.datetime.now()
        prettyfy=str(root_ct.prettify())
        for i in range(len(prettyfy)):
            prettyfy[i]="A"
        print(datetime.datetime.now()-now)

        items_ct = []
        tags_ct = root_ct.find_all(class_="\'model-short-block\'")  # поиск по предложениям
        i = 0
        for tag in tags_ct:  # создание объектов продукта
            items_ct.append(product_eKatalog(str(tag)))
            items_ct[i].to_string()
            i += 1
            print(
                "____________________________________________________________________________________________________________________________________________________")
        return items_ct


class product_eKatalog:
    def __init__(self, js__subcategory_product_item):

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
                description = str(description[i:len(description) - 1])
                break
            if w == ";":
                flag_d = True
            i += 1
        description = description.strip(" ")

        self.link = link_attr["href"]
        self.image = image_attr["data-src"]
        self.name = decoded["shortName"]
        self.price = decoded["price"]
        self.description = description

        pass

    def to_string(self):
        print("Название товара:\t\t\t" + str(self.name))
        print("Цена товара:\t\t\t\t" + str(self.price))
        print("Ссылка на картинку :\t\t" + str(self.image))
        print("Ссылка на продукт товара:\t" + str(self.link))
        print("Описание товара:\t" + str(self.description.strip(' ')))


if __name__ == '__main__':
    # y_req = input("Введите ваш запрос:\t")
    # y_req = str(y_req.replace(' ', '+'))
    # print(y_req)
    y_req="телефон+xiaomi+redmi"
    ps = get_eKatalog()

    # try:
    items_ct = ps.get_products_eKatalog(y_req)
    # except:
    #     print("Была какая-то ошибка, но норм..")

    print(f'Search {y_req!r}...')

    # print(len(items_ct))
    # print(f'  Result ({len(items_ct)}):')
    # for title, url in items_ct:
    #     print(f'    {title!r}: {url}')