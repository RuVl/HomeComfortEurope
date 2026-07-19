import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from config import CHROMEDRIVER_PATH, WINDOW_SIZE


def get_driver(folder: str):
    service = Service(CHROMEDRIVER_PATH)
    options = Options()

    # options.add_argument("--headless")
    options.add_argument(f"--window-size={WINDOW_SIZE}")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    options.add_experimental_option("prefs", {
        "download.default_directory": folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    logging.debug('Starting driver...')

    return webdriver.Chrome(options=options, service=service)