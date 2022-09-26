from unicodedata import digit
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def scraper(Yt_link):
    driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"))
    driver.get(Yt_link)
    try:
        views = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='view-count style-scope ytd-video-view-count-renderer']")))
    except:
        views = -1
    try:
        name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='title style-scope ytd-video-primary-info-renderer']")))
    except:
        name = None
    integer_views = re.findall(r'\b\d+\b', views.text)
    final_views= ''.join(integer_views)
    final_name = name.text
    driver.close()
    return final_views,final_name