from selenium.webdriver.chrome.webdriver import WebDriver
from Utilities.lib import SeleniumWrapper
from time import sleep

class TestProduct:
    def test_search_product(self):
        driver = WebDriver()
        driver.get("http://49.249.28.218:8081/AppServer/Online_Shopping_Application/")
        driver.maximize_window()
        wrapper = SeleniumWrapper(driver)
        wrapper.click_element(('xpath', "//input[@class='search-field']"))
        wrapper.click_element(("xpath","//li[@class='dropdown yamm']//a[contains(text(),'Furniture')]"))
        sleep(10)

















