from selenium import webdriver

from bs4 import BeautifulSoup
from time import time


class magazine_name_price:
    def __init__(self,name,price:str,link):
        self.name=name
        self.price=int(price.replace("\xa0","").replace("р.",""))
        self.link=link


class reviews:                                                                                                                                  #new
    def __init__(self,stars:str="0,0,0,0"):
        if stars:
            splitter=stars.split(',')
            self.terribly=splitter[0]
            self.bad = splitter[1]
            self.good=splitter[2]
            self.nice=splitter[3]


class unexpected:                                                                                                                                  #new
    def __init__(self,html_data:str):
        soup = BeautifulSoup(html_data, 'html.parser')
        # self.title=soup.get('title')
        self.title=soup.find('span',class_='brand-cat-pict').get('title')
        # self.link=soup.get('href')
        self.link='https://www.e-katalog.ru'+soup.find('span',class_='brand-cat-pict').get('href')



class Product_eKatalog:
    def __init__(self,html_data:str):
        soup = BeautifulSoup(html_data, 'html.parser')
        # selsectedTag = soup.find('a', {"title": True})
        # self.name=selsectedTag.text  - если нам нужно имя "без типа", например "xiaome redmi", а не "Моб. телефон... x. r."
        selsectedTag=soup.find('img',{"src":True})
        self.image_Link='https://www.e-katalog.ru'+selsectedTag.attrs["src"]
        self.name=selsectedTag.attrs['alt'] # там словарь, просто вытаскиваю

        self.magazines=soup.find_all('td',class_='model-shop-name')
        self.magazines_price=soup.find_all('td',class_='model-shop-price')
        # self.magazines_tr=soup.find_all('tr')

        self.data_about_magazines=[]
        self.description=soup.find('div',class_='model-short-description').get('data-descr')                                                                 # new
        stars=str(soup.find('td',class_='short-opinion-icons').find_all('sub')).replace("<sub>","").replace("</sub>","").replace('[',"").replace(']','')     # new
        self.review=reviews(stars)                                                                                                                           # new
        count_pricer=0
        for magazine in self.magazines:
            data_magazine=BeautifulSoup(str(magazine),'html.parser')   # .contents[0]
            data_magazine_price=BeautifulSoup(str(self.magazines_price[count_pricer]), 'html.parser')   # .contents[0]
            link=data_magazine.find('a').get('onmouseover') # беру содержимое атрибута
            #
            # end_href = link.index()
            # new_tag = link[11:end_href]
            newl=str(link).split('"')
            self.data_about_magazines.append(magazine_name_price(data_magazine.find('a').find('u').text,data_magazine_price.find('a').text,str(newl[1])))
            count_pricer+=1
            flag=True

        prettify = soup.prettify()


        # for magazine in self.magazines_tr:
        #     data_magazine = BeautifulSoup(str(magazine.contents), 'html.parser')
        #     pret=data_magazine.prettify()
        #     flag = True

        # for magazine in self.magazines_tr.contents[0]:
        #     data_magazine=BeautifulSoup(str(magazine),'html.parser')   # .contents[0]
        #     self.data_about_magazines.append(magazine_name_price(data_magazine.find('a').find('u').text,'465'))
        #     flag=True
    def ToString(self):
        print("Продукт: "+self.name)
        print("Ссылка на картинку: "+self.image_Link)
        print("Описание: "+self.description)
        print("Отзывы: "+str(self.review.__dict__))
        print("Магазины и цены: ")
        for i in self.data_about_magazines:
            print(i.__dict__)

    def search_href(self,tag='this.href="https://www.e-katalog.ru/clcp.php?ep_=7DQ4031J59131J35131J514J1J3I231J49331J101J1J51331J074J1J35131J08531J0A231J36531J0Q0J1J51531J0Q0313714J1J524J&model_=Xiaomi+Redmi+Note+9+128GB&idSite_=1&idGood_=1784026";this.onmouseover=null;this.removeAttribute("onmouseover");'):
        end_href=tag.index()
        new_tag=tag[11:end_href]
        return new_tag










startDriver=time()
chromedriver = 'C:\\Users\\Asus\\Desktop\\GachiParser\\parser\\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)


target=input("Введите однозначное название товара: ").replace(' ','+')
url = f'https://www.e-katalog.ru/ek-list.php?search_={target}'
browser.get(url)
# browser.get('https://www.e-katalog.ru/ek-list.php?search_=xiaomi+redmi+note+7')




html_data=browser.page_source
soup = BeautifulSoup(html_data, 'html.parser')


# Тут обрабатывается возможные неопределенные отоброжения ( например, продукты бренда)
uncertain_req = soup.find_all('div',class_='brand-cat-div')
unexpected_items=[]
if not uncertain_req:                                                                         #new
    tags = soup.find_all('table', class_='model-short-block')  # поиск по предложениям
else:
    for select in uncertain_req:
        unexpected_items.append(unexpected(str(select)))
    print('Неопределенный результат, уточните поиск')
    print('Тут юзер выбирает категорию')

    print('Нажал на нужную')
    new_link=unexpected_items[0].link
    url = new_link  # url присваивается поле link Выбранного элемента
    browser.get(url)  # делается запрос
    html_data = browser.page_source  # хттмл
    new_soup = BeautifulSoup(html_data, 'html.parser')
    tags = new_soup.find_all('table', class_='model-short-block')  # поиск по предложениям
for case in unexpected_items:
    print(case.__dict__)


# далее идёт поиск как будто всё норм и выборка


items = []
for element in tags:
    items.append(Product_eKatalog(str(element)))

for i in (items):
    i.ToString()
    print("__________________________________________________________________________________________________________________")


assert "No results found." not in browser.page_source

browser.quit()



