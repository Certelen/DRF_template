from datetime import datetime
from time import sleep
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

from api.models import Ad, Check
from drf_project.settings import URL, BROWSER_LOCATION


logger = logging.getLogger(__name__)


def check_bot(driver):
    try:
        if driver.find_element(By.XPATH, '//div[starts-with(@class, "cap")]'):
            logger.error('Требуется пройти верификацию от робота')
            driver.close()
            driver.quit()
            return True
    except NoSuchElementException:
        return False


def update_ads():
    options = Options()
    options.add_argument("--log-level=1")
    options.binary_location = BROWSER_LOCATION
    driver = webdriver.Chrome(options=options, service=ChromeService(
        ChromeDriverManager().install()))

    driver.get(URL)
    driver.maximize_window()
    sleep(10)
    if check_bot(driver):
        return
    ads = driver.find_elements(By.XPATH, '//tr[@data-source="actual"]')
    for index in range(10):
        id_number = ads[index].find_element(
            By.TAG_NAME, 'a').get_attribute("name")
        position = index + 1
        viewing = ads[index].find_element(
            By.TAG_NAME, 'span').text
        title = ads[index].find_element(
            By.CLASS_NAME, 'bulletinLink'
        )
        link = title.get_attribute("href")
        title = title.text
        driver.get(link)
        sleep(5)
        if check_bot(driver):
            return
        author = driver.find_element(
            By.CLASS_NAME, 'userNick'
        ).find_element(By.TAG_NAME, 'a').text
        values_for_update = {
            'id': position,
            'id_number': id_number,
            'position': position,
            'viewing': viewing,
            'title': title,
            'author': author
        }
        Ad.objects.update_or_create(
            position=position,
            defaults=values_for_update
        )
        logger.warning(f'Успешно спарсил объявления на позиции #{position}')
        driver.execute_script("window.history.go(-1)")
    Check.objects.create(
        last_check=datetime.now()
    )
    driver.close()
    driver.quit()
