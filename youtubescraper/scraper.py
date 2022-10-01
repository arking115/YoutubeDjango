from unicodedata import digit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class scraper:
    def __init__(self, yt_link):
        self.driver = webdriver.Chrome()
        self.yt_link = yt_link
        self.url_info=[]

    def get_name(self, yt_link):
        self.driver.get(yt_link)
        try:
            name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='title style-scope ytd-video-primary-info-renderer']")))
        except:
            name = None
        name = name.text
        return name

    def get_views(self):
        try:
            views = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='view-count style-scope ytd-video-view-count-renderer']")))
        except:
            views = -1
        integer_views = re.findall(r'\b\d+\b', views.text)
        final_views= ''.join(integer_views)
        final_views = int(final_views)
        return final_views

    #def get_info(self, yt_url):
      #  self.driver.get(yt_url)
       # try:
       #     views = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='view-count style-scope ytd-video-view-count-renderer']")))
       # except:
       #     views = -1
       # try:
       #     name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='title style-scope ytd-video-primary-info-renderer']")))
       # except:
       #     name = None
       # views = views.text
       # name = name.text
       # return views, name

    def extract_url_info(self):
        self.url_info.append(self.get_name(self.yt_link))
        self.url_info.append(self.get_views())
        self.driver.close()
    
    def run(self):
        self.extract_url_info()
        print(self.url_info)

yt = scraper('https://www.youtube.com/watch?v=mcp-6mAnOnA')
yt.run()
