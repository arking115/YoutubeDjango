from ssl import VERIFY_ALLOW_PROXY_CERTS
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
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                (By.XPATH, "//h1[@class='style-scope ytd-watch-metadata']"))
            )
            name = self.driver.find_element(
                By.XPATH, "//h1[@class='style-scope ytd-watch-metadata']"
            )
            name = name.text
        except:
            name = None

        try:
            name = self.driver.find_element(
                By.XPATH, "//yt-formatted-string[@class='style-scope ytd-reel-player-header-renderer']"
            )
            name = name.text
        except:
            pass

        return name
        #2 - > style-scope ytd-watch-metadata
        #1 - > title style-scope ytd-video-primary-info-renderer


    def get_views(self):
        try:
            # Wait till element is present
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                (By.XPATH, "//yt-formatted-string[@id='info']"))
            )
            # Get element
            views = self.driver.find_element(
                By.XPATH, "//yt-formatted-string[@id='info']"
            )
            right_lim = views.text.find("views") - 1
            views = views.text[:right_lim]
            integer_views = re.findall(r'\b\d+\b', views)
            final_views = ''.join(integer_views)
            views = int(final_views)
        except:
            views = 0

        return views
        #1 - > view-count style-scope ytd-video-view-count-renderer


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


    def consent(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                (By.XPATH, "//button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--call-to-action yt-spec-button-shape-next--size-m ']"))
            )
            consent_button = self.driver.find_element(By.XPATH, "//button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--call-to-action yt-spec-button-shape-next--size-m ']")
        except:
            consent_button = 0

        try:
            consent_button_2 = self.driver.find_element(By.XPATH, "//button[@aria-label='Reject all']")
        except:
            consent_button_2 = 0

        if consent_button != 0:
             consent_button.click()
        if consent_button_2 != 0:
            consent_button_2.click()
        try:
            views_button = self.driver.find_element(By.XPATH, "//tp-yt-paper-button[@id='expand']")
            views_button.click()
        except:
            pass
    
    def close_popup(self):
        handles = self.driver.window_handles
        yt_page_handle = self.driver.current_window_handle
        for handle in handles:
            if handle != yt_page_handle:
                self.driver.switch_to.window(handle)
                self.driver.close()
        self.driver.switch_to.window(yt_page_handle)

    def get_youtube_link_info(self, youtube_link):
        self.driver.get(youtube_link)
        self.consent()
        self.close_popup()
        views = self.get_views()
        name = self.get_name()
        return name, views
#https://www.youtube.com/watch?v=GwTqzwz7I5M