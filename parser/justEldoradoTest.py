from bs4 import BeautifulSoup
import json
import requests


class Product_eldorado:
    name = "eldorado"
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
        #test = requests.get(url)
        #print(test.content)
        # data_eldorado = response_eldorado.json()                  # переводим в json
        # print(response_eldorado)

        bs_eldorado = BeautifulSoup(response_eldorado.content, 'html.parser')
        items_eldorado = []
        tags_ct = bs_eldorado.find_all(class_="sc-1w9a1pg-0 sc-19ibhqc-0 gUmybO")  # поиск по предложениям
        i = 0
        for tag in tags_ct:  # создание объектов продукта
            items_eldorado.append(Product_eldorado(str(tag)))
            items_eldorado[i].to_string()
            i += 1
            print(
                "____________________________________________________________________________________________________________________________________________________")
        return items_eldorado

if __name__=="__main__":
    testEldorado = get_eldorado()
    testEldorado.get_products_eldorado("xiaomi+redmi")