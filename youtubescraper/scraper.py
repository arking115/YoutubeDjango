from unicodedata import digit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_name(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//h1[@class='title style-scope ytd-video-primary-info-renderer']"))
            )
            name = self.driver.find_element(
                By.XPATH, "//h1[@class='title style-scope ytd-video-primary-info-renderer']"
            )
            name = name.text
        except:
            name = None

        return name

    def get_views(self):
        try:
            # Wait till element is present
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//span[@class='view-count style-scope ytd-video-view-count-renderer']"))
            )
            # Get element
            views = self.driver.find_element(
                By.XPATH, "//span[@class='view-count style-scope ytd-video-view-count-renderer']"
            )
            integer_views = re.findall(r'\b\d+\b', views.text)
            final_views = ''.join(integer_views)
            views = int(final_views)
        except:
            views = None

        return views

    def get_youtube_link_info(self, youtube_link):
        self.driver.get(youtube_link)
        views = self.get_views()
        name = self.get_name()
        return name, views
