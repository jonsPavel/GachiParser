from selenium import webdriver

from bs4 import BeautifulSoup
from time import time


class magazine_name_price:
    def __init__(self,name,price:str,link):
        self.name=name
        self.price=int(price.replace("\xa0","").replace("р.",""))
        self.link=link




class Product_eKatalog:
    def __init__(self,html_data:str):
        soup = BeautifulSoup(html_data, 'html.parser')
        # selsectedTag = soup.find('a', {"title": True})
        # self.name=selsectedTag.text  - если нам нужно имя "без типа", например "xiaome redmi", а не "Моб. телефон... x. r."
        selsectedTag=soup.find('img',{"src":True})
        self.image_Link='https://www.e-katalog.ru'+selsectedTag.attrs["src"]
        self.name=selsectedTag.attrs['alt']

        self.magazines=soup.find_all('td',class_='model-shop-name')
        self.magazines_price=soup.find_all('td',class_='model-shop-price')
        # self.magazines_tr=soup.find_all('tr')

        self.data_about_magazines=[]

        count_pricer=0
        for magazine in self.magazines:
            data_magazine=BeautifulSoup(str(magazine),'html.parser')   # .contents[0]
            data_magazine_price=BeautifulSoup(str(self.magazines_price[count_pricer]), 'html.parser')   # .contents[0]
            link=data_magazine.find('a').get('onmouseover')
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
        print("Магазины и цены: ")
        for i in self.data_about_magazines:
            print(i.__dict__)

    def search_href(self,tag='this.href="https://www.e-katalog.ru/clcp.php?ep_=7DQ4031J59131J35131J514J1J3I231J49331J101J1J51331J074J1J35131J08531J0A231J36531J0Q0J1J51531J0Q0313714J1J524J&model_=Xiaomi+Redmi+Note+9+128GB&idSite_=1&idGood_=1784026";this.onmouseover=null;this.removeAttribute("onmouseover");'):
        end_href=tag.index()
        new_tag=tag[11:end_href]
        return new_tag

    def fun(request):
        startDriver = time()
        chromedriver = 'chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
        endDriver = time()

        startGet = time()
        target = request.POST.get('param').replace(' ', '+')
        url = f'https://www.e-katalog.ru/ek-list.php?search_={target}'
        browser.get(url)
        # browser.get('https://www.e-katalog.ru/ek-list.php?search_=xiaomi+redmi+note+7')
        endGet = time()

        startBS = time()
        html_data = browser.page_source
        soup = BeautifulSoup(html_data, 'html.parser')
        tags = soup.find_all('table', class_='model-short-block')  # поиск по предложениям
        endBS = time()

        items = []
        for element in tags:
            items.append(Product_eKatalog(str(element)))

        browser.quit()
        return (items)












