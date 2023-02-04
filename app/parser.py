import os
import os.path
import uuid


import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from models import db, Apartments
from __init__ import create_app

app = create_app()

def scrape():
    #ВКЛЮЧЕНИЕ HEADLESS-РЕЖИМА
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(
        options=options,
        service=ChromeService(ChromeDriverManager().install()),
    )


    driver.get("https://www.avito.ru/moskva/kvartiry/prodam-ASgBAgICAUSSA8YQ?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyNLNSKk5NLErOcMsvyg3PTElPLVGyrgUEAAD__xf8iH4tAAAA&f=ASgBAQICAUSSA8YQAUDKCKSKWZqsAZisAZasAZSsAYhZhlmEWYJZgFk")
    apartments = driver.find_elements(By.CLASS_NAME, "items-items-kAJAg")

    for apartment in apartments:
        try:
            title = apartment.find_element(By.CLASS_NAME, 'link-link-MbQDP').text
            url = apartment.find_element(By.CLASS_NAME, 'link-link-MbQDP').get_attribute('href')
            price = apartment.find_element(By.CSS_SELECTOR, "meta[itemprop='price']").get_attribute('content')

            print(title, url, price)


            wait = WebDriverWait(driver, 1)
            link = apartments[0].find_element(By.CLASS_NAME, "iva-item-root-_lk9K")

            link = wait.until(expected_conditions.element_to_be_clickable(link))

            link.click()

            driver.switch_to.window(driver.window_handles[-1])



            image = wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "css-1qr5gpo")))

            image_url = image.get_attribute('src')

            img_data = requests.get(image_url).content
            filename = str(uuid.uuid4())

            filename_path = f'photos/{filename}.jpg'

            with open(filename_path, 'wb') as handler:
                handler.write(img_data)

            abs_path = str(os.path.abspath(img_data))

            save_avito_ads(title, url, price, image_url, filename_path)

        except NoSuchElementException:
            # If the data is missing, skip this flat
            continue

    driver.close()

def save_avito_ads(title, url, price, image_url, image_path):
    new_apartment = Apartments(
        title=title,
        url=url,
        price=price,
        image_url=image_url,
        image_path=image_path,
    )
    with app.app_context():
        db.session.add(new_apartment)
        db.session.commit()


with app.app_context():
    scrape()


