from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import urllib
import os
import time

NAVER = "https://search.naver.com/search.naver?where=image&section=image&query=돈명언"
NUM = 100

PACK = By.CLASS_NAME, "main_pack"


def open_browser(url, num):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    imgs = browser.find_elements_by_class_name("_img")
    wait = WebDriverWait(browser, 10)

    while len(imgs) < num:
        time.sleep(1)
        max_height = "document.body.scrollHeight"
        browser.execute_script(f"window.scrollBy(0, {max_height});")
        wait.until(EC.presence_of_element_located(PACK))
        imgs = browser.find_elements_by_class_name("_img")
        if len(imgs) >= num:
            html = browser.execute_script("return document.body.outerHTML;")
            browser.close()
            soup = BeautifulSoup(html, 'html.parser')
            imgs = soup.select("._img")
            imgs = imgs[:num]
            break
    return imgs

def get_imgs(html):

    os.mkdir("돈명언")

    for img in imgs:

        while True:
            try:
                urllib.request.urlretrieve(img['src'], f"돈명언/{imgs.index(img)}.jpg")
            except Exception:
                print(f"{imgs.index(img)}--invalid")
                continue
            break
    return


imgs = open_browser(NAVER, NUM)
get_imgs(imgs)