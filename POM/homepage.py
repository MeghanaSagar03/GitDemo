from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from Utilities.lib import SeleniumWrapper


class HomePage:
   click_login = ("link text", "Login")
   search_bar = ("class", "search-field")
   search_icon= ("class", "search-button")
   click_product=("class","contains(text(),'Furniture')")

   def __init__(self, driver):
       self.driver = driver
       self.wrapper = SeleniumWrapper(self.driver)

   def click_login(self):
       self.wrapper.click_element((self.click_login))

   def search(self):
      self.wrapper.click_element(self.search_bar)

   def icon(self):
       self.wrapper.click_element(self.search_icon)

   def product(self):
       self.wrapper.click_element(self.click_product)