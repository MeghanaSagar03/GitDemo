from selenium.webdriver.chrome.webdriver import WebDriver

from POM.loginpage import LoginPage
from Utilities.lib import SeleniumWrapper
# from Utilities.excel_lib import read_headers, read_data
# from pytest import mark
# from POM.loginpage import LoginPage


# headers1 = read_headers("smoke", "test_login_positive")
# data1 = read_data("smoke", "test_login_positive")
#
#
# @mark.parametrize(headers1, data1)
# def test_login_positive(_config, pages, email, password):
#     pages.loginpage.login(email, password)
#     assert True == pages.loginpage.is_user_logged_in(email), f"the user {email} login was not successfull"
#
#
# headers2 = read_headers("smoke", "test_login_negative")
# data2 = read_data("smoke", "test_login_negative")
#
# @mark.parametrize(headers2, data2)
# def test_login_negative(_config, pages, email, password):
#     # pages.load()
#     # pages.loginpage.click_login()
#     pages.loginpage.login(email, password)
#     assert False == pages.loginpage.is_user_logged_in(email)


## WITHOUT-DATA DRIVEN CODE
class TestLogin:
    def test_login(self):
        driver = WebDriver()
        driver.get("http://49.249.28.218:8081/AppServer/Online_Shopping_Application/")
        driver.maximize_window()
        wrapper = SeleniumWrapper(driver)
        wrapper.click_element(('xpath', "//a[@href='login.php']"))
        wrapper.click_element(("name", "email"))
        wrapper.enter_text(("name", "email"), value="anuj.lpu1@gmail.com")
        wrapper.click_element(("id", "exampleInputPassword1"))
        wrapper.enter_text(("id", "exampleInputPassword1"), value="Test@123")
        wrapper.click_element(("link text", "Login"))
        driver.close()
