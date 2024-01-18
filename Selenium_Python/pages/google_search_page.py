from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleSearchPage:

    SEARCH_RESULTS_SELECTOR = 'h3'

    def __init__(self, driver):
        self.driver = driver

    def search(self, query):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.submit()

    def setup_the_page(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.google.com")
        self.google_search_page = GoogleSearchPage(self.driver) 

    def click_first_result(self):
        first_result = self.driver.find_element(By.CSS_SELECTOR, self.SEARCH_RESULTS_SELECTOR)
        first_result.click()