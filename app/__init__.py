import os
import os.path
import uuid

import requests
from flask import Flask, render_template, send_from_directory, url_for
from flask_sqlalchemy import SQLAlchemy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from models import db, Apartments

#app = Flask(__name__)
#db = SQLAlchemy()
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
#db.init_app(app)

def create_app() -> object:
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return 'Weird Appartment Finder!'

    return app

#engine = create_engine('sqlite:///avito.db')
#Session = sessionmaker(bind=engine)
#session = Session()


#class Apartments(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #title = db.Column(db.String(100))
    #url = db.Column(db.String(100))
    #price = db.Column(db.Integer)
    #image_url = db.Column(db.String(100))
    #image_path = db.Column(db.String(1000))

    #def __init__(self, title, url, price, image_url, image_path):
        #self.title = title
        #self.url = url
        #self.price = price
        #self.image_url = image_url
        #self.image_path = image_path

    #def __repr__(self):
        #return '<Apartments %r>' % self.title


#def save_to_db(title, url, price, image_url, image_path):
    #product = Product(title=title, url=url, price=price, image_url=image_url, image_path=image_path)
    #db.session.add(product)
    #db.session.commit()

#def scrape():
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    #driver.get("https://www.avito.ru/moskva/kvartiry/prodam-ASgBAgICAUSSA8YQ?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA&f=ASgBAQICAUSSA8YQAUDKCKSKWZqsAZisAZasAZSsAYhZhlmEWYJZgFk")
    #apartments = driver.find_elements(By.CLASS_NAME, "items-items-kAJAg")

    #for apartment in apartments:
        #title = apartment.find_element(By.CLASS_NAME, 'link-link-MbQDP').text
        #url = apartment.find_element(By.CLASS_NAME, 'link-link-MbQDP').get_attribute('href')
        #price = apartment.find_element(By.CSS_SELECTOR, "meta[itemprop='price']").get_attribute('content')

        #print(title, url, price)


        #wait = WebDriverWait(driver, 3)
        #link = apartments[0].find_element(By.CLASS_NAME, "iva-item-root-_lk9K")
        #print(link.get_attribute('href'))
        #link = wait.until(expected_conditions.element_to_be_clickable(link))
        #print(link.get_attribute('href'))
        #link.click()

        #driver.switch_to.window(driver.window_handles[-1])
        #image = driver.find_element(By.CLASS_NAME, "css-1qr5gpo")

        #НАЙТИ ЭЛЕМЕНТ ИЗОБРАЖЕНИЯ
        #image = wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "css-1qr5gpo")))

        # ПОЛУЧИТЬ URL из документа
        #image_url = image.get_attribute('src')

        #img_data = requests.get(image_url).content
        #filename = uuid.uuid4().hex
        #with open(f'photos/{filename}.jpg', 'wb') as handler:
            #handler.write(img_data)

            #abs_path = str(os.path.abspath(img_data))
            #image_path = abs_path.encode("utf-8")
            #print(image_url)
        #save_avito_ads(title, url, price, image_url, image_path)
    #driver.close()

#def save_avito_ads(title, url, price, image_url, image_path):
    #new_apartment = Apartments(
        #title=title,
        #url=url,
        #price=price,
        #image_url=image_url,
        #image_path=abs_path_utf8,
    #)
        #with app.app_context():
            #db.create_all()
    #db.session.add(new_apartment)
    #db.session.commit()




if __name__ == '__main__':
    #create_app()
    scrape()
    app.run(debug=True)