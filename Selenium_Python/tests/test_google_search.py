import unittest
from selenium import webdriver
from google_search_page import GoogleSearchPage

## This is a sample of the first scenario using unittest
class TestGoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='driver\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("https://www.google.com")
        self.google_search_page = GoogleSearchPage(self.driver)

    def test_google_search(self):
        query = 'test automation'
        self.google_search_page.search(query)
        self.assertIn(query, self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()