from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from Utilities.lib import SeleniumWrapper

#WITHOUT USING DATA DRIVEN METHOD

class TestAccount:   # Note=>While running this test case change all the values for create account
    def test_createAcoount(self):
        driver = WebDriver()
        driver.get("http://49.249.28.218:8081/AppServer/Online_Shopping_Application/")
        driver.maximize_window()
        wrapper = SeleniumWrapper(driver)
        wrapper.click_element(('xpath', "//a[@href='login.php']"))
        wrapper.click_element(("id", "fullname"))
        wrapper.enter_text(("id","fullname"),value="SreeRakshaa")
        wrapper.click_element(("id" , "email"))
        wrapper.enter_text(("id","email"),value="shree.108@gmail.com")
        # wrapper.page_up(("id","contactno"),value="9876542211")
        # # sleep(2)
        driver.execute_script("window.scrollBy(0,500)","")
        wrapper.click_element(("id","contactno"))
        wrapper.enter_text(("id","contactno"),value="9876540007")
        wrapper.click_element(("id","password"))
        wrapper.enter_text(("id","password"),value="Shree@0018")
        wrapper.click_element(("id","confirmpassword"))
        wrapper.enter_text(("id","confirmpassword"),value="Shree@0018")
        # driver.execute_script("window.scrollBy(0,200)", "")
        wrapper.click_element(("name","submit"))



