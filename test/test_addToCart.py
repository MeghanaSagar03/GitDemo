from selenium.webdriver.chrome.webdriver import WebDriver
from Utilities.lib import SeleniumWrapper
from time import sleep


class TestAddToCart:
    def test_addToCart(selfself):
        driver = WebDriver()
        driver.get("http://49.249.28.218:8081/AppServer/Online_Shopping_Application/category.php?cid=5")
        driver.maximize_window()
        wrapper = SeleniumWrapper(driver)
        driver.execute_script("window.scrollBy(0,600)", "")
        sleep(5)
        wrapper.click_element(("xpath","(//button[@class='btn btn-primary'])[1]"))
        sleep(10)