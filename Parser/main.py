import json
import logging
import time
import traceback
from pathlib import Path

import tqdm
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from utils import get_driver
from config import *


def login(driver: webdriver.Chrome):
    driver.get(f"{SITE}register.php")

    # Log in
    driver.find_element(By.ID, "toggle4").click()
    time.sleep(1)

    driver.find_element(By.ID, "RemailId").send_keys(LOGIN)
    driver.find_element(By.ID, "Rusrpassword").send_keys(PASSWORD + Keys.ENTER)


def get_types(el: WebElement) -> dict:
    types = {}
    for li in el.find_element(By.CLASS_NAME, "submenu").find_elements(By.TAG_NAME, "li"):
        a = li.find_element(By.TAG_NAME, "a")
        types[a.get_attribute("title")] = a.get_attribute("href")

    return types


def get_category_info(driver: webdriver.Chrome, xpath: str) -> dict:
    driver.get(SITE)

    category_a_el = driver.find_element(By.XPATH, xpath).find_element(By.TAG_NAME, 'a')
    category_name = category_a_el.get_attribute('innerText')



    types_url = get_types(driver.find_element(By.XPATH, xpath))

    # all_products[top] = {}
    # for type_, url in tqdm.tqdm(urls.items()):
    #     driver.get(url)
    #
    #     product_urls = []
    #     for li in driver.find_element(By.ID, "myList").find_elements(By.TAG_NAME, "li"):
    #         product_urls.append(li.find_element(By.TAG_NAME, "a").get_attribute("href"))
    #
    #     # all_products[top][type] = {}
    #     for u in product_urls:
    #         product = {}
    #
    #         driver.get(u)
    #         desc = driver.find_element(By.CLASS_NAME, "right-description")
    #
    #         name = desc.find_element(By.TAG_NAME, "h1").text
    #         for tr in desc.find_elements(By.TAG_NAME, "tr"):
    #             prop, *_, val = tr.find_elements(By.TAG_NAME, "td")
    #             product[prop.text] = val.text
    #
    #         all_products[top][type][name] = product
    #
    #         all_products[top][type]['description'] = driver.find_element(By.CLASS_NAME, 'leftDiv').get_attribute('innerHTML')
    #         image_url = driver.find_element(By.ID, "product").get_attribute("href")
    #
    #         def to_path(path: str):
    #             return path\
    #                 .replace(' ', '_')\
    #                 .replace('"', '')\
    #                 .replace("'", '')\
    #                 .replace('\\', '')\
    #                 .replace('/', '')\
    #                 .replace('?', '')\
    #                 .replace(':', '')\
    #                 .replace('*', '')\
    #                 .replace('<', '')\
    #                 .replace('>', '')\
    #                 .replace('|', '')
    #
    #         driver.get(image_url)
    #         with open(img_folder / f"{to_path(name)}.png", 'wb') as f:
    #             f.write(driver.find_element(By.TAG_NAME, "img").screenshot_as_png)


def main():
    img_folder = Path(IMAGE_FOLDER)

    with get_driver(str(img_folder.absolute())) as driver:
        try:
            login(driver)

            topics = [
                "/html/body/header/div/div/nav/ul/li[3]",
                "/html/body/header/div/div/nav/ul/li[4]",
                "/html/body/header/div/div/nav/ul/li[5]"
            ]

            all_products = {}
            for topic in topics:
                all_products.update(get_category_info(driver, topic))

            with open("products.json", "w") as f:
                json.dump(all_products, f, ensure_ascii=True, indent=4)
        except:
            logging.error(traceback.format_exc())
            input("Press enter to close app...\n")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
