from unicodedata import digit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re, time


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

    def get_channel_videos(self, channel_link):
        self.driver.get(channel_link)
        i=1
        scroll_pause_time = 0.8
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                 (By.ID, "items"))
             )
        #Scrolling to the bottom of the channel's video section
        last_height = self.driver.execute_script("return document.documentElement.scrollHeight")
        while i == 1:
            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = self.driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                i = 0
            last_height = new_height
        #Making a list of all the hrefs present on the video section of the channel
        vid_links = self.driver.find_elements(By.ID, "video-title")
        vid_links_f = []
        for vid_link in vid_links:
            vid_links_f.append(vid_link.get_attribute("href"))
        return vid_links_f

    def get_youtube_link_info(self, youtube_link):
        self.driver.get(youtube_link)
        views = self.get_views()
        name = self.get_name()
        return name, views
scraper = Scraper()
scraper.get_youtube_link_info("https://www.youtube.com/watch?v=6WVx-gMshYc")