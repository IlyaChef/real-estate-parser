import os
import os.path
import uuid
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from models import db, Flat
from yarl import URL
from __init__ import create_app
from functions import is_carpet, is_leopard, is_scand


app = create_app()

def parse_page():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(
        #options=options,
        service=ChromeService(ChromeDriverManager().install()),
    )
    base_url = URL("https://www.avito.ru")
    region = "all"
    category = "kvartiry"
    rent = "sdam"
    term = "na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg"
    q = "косметический+ремонт"
    url = base_url / region / category / rent / term % {'cd': '1', 'q': q}
    driver.get(str(url))

    # Find all the flats on the page
    flats = driver.find_elements(By.CLASS_NAME, "iva-item-root-_lk9K")

    for flat in flats:
        try:
            flat_link = flat.find_element(By.XPATH, ".//*[@data-marker='item-title']")

            flat_url = flat_link.get_attribute("href")
            flat_name = flat_link.get_attribute("title")
            print(flat_url)
            print(flat_name)
            flat_image = flat.find_element(By.XPATH, ".//*[@data-marker='item-photo']//img")
            flat_image_url = flat_image.get_attribute("src")
            flat_image_content = requests.get(flat_image_url).content
            flat_image_dir = app.config['MEDIA_PATH']

            if not os.path.exists(flat_image_dir):
                os.makedirs(flat_image_dir)
            flat_image_filename = f'{uuid.uuid4().hex}.jpg'
            filename_path = f'media/{flat_image_filename}'

            with open(f"{flat_image_dir}/{flat_image_filename}", 'wb') as f:
                f.write(flat_image_content)

            carpet_bool, carpet_coeff = is_carpet(f"{flat_image_dir}/{flat_image_filename}")
            #scand_bool, scand_coeff = is_scand(f"{flat_image_dir}/{flat_image_filename}")
            #leopard_bool, leopard_coeff = is_leopard(f"{flat_image_dir}/{flat_image_filename}")

            # Save the data to the database
            new_flat = Flat(
                title=flat_name,
                image=flat_image_url,
                url=flat_url,
                flat=filename_path,
                is_grandma=True if 'True' == carpet_bool else False,
                grandma=float(carpet_coeff),
                # is_scandy=True if 'True' == scand_bool else False,
                # scandy=float(scand_coeff),
                # is_leopard=True if 'True' == leopard_bool else False,
                # leopard=float(leopard_coeff),
            )



            db.session.add(new_flat)
            db.session.commit()

        except NoSuchElementException:
            # If the data is missing, skip this flat
            continue
if __name__ == '__main__':
    is_scandi=True
    is_carpet_wall=True
    with app.app_context():
        parse_page()




