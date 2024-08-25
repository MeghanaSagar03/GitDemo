from pytest import fixture
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.edge.webdriver import WebDriver as Edge
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from POM.homepage import HomePage
from POM.loginpage import LoginPage
from test.test_addToCart import TestAddToCart
from test.test_createAccount import TestAccount


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", dest="browser") #browser
    parser.addoption("--env", action="store", default="test", dest="env") # environment
    parser.addoption("--headless", action="store_true", dest="headless", default=False) # excel


@fixture
def _config(request):
    class TestConfigurations:
        url = "http://49.249.28.218:8081/AppServer/Online_Shopping_Application/"
        email = "anuj.lpu1@gmail.com"
        password = "Test@123"

    class StageConfigurations:
        url = "http://49.249.28.218:8081/AppServer/Online_Shopping_Application/"
        email = "anuj.lpu1@gmail.com"
        password = "Test@123"

    exe_env = request.config.option.env

    if exe_env.upper() == "TEST":
        print("Execution evironment is TEST")
        return TestConfigurations()
    elif exe_env.upper() == "STAGE":
        print("Execution environment is STAGE")
        return StageConfigurations()
    else:
        raise Exception("Invalid execution environment")

@fixture
def driver(request, _config):
    browser_name = request.config.option.browser
    is_headless = request.config.option.headless
    options = None
    print("executing setup")
    if browser_name.upper() == "CHROME":
        if is_headless:
            options = ChromeOptions()
            options.add_argument("--headless=new")
        _driver = Chrome(options=options)
    elif browser_name.upper() == "FIREFOX":
        if is_headless:
            options = FirefoxOptions()
            options.add_argument("--headless")
        _driver = Firefox(options=options)
    elif browser_name.upper() == "EDGE":
        if is_headless:
            options = EdgeOptions()
            options.add_argument("--headless=new")
        _driver = Edge(options=options)
    else:
        raise Exception("Invalid browser")
    _driver.get(_config.url)
    _driver.maximize_window()
    yield _driver
    print("executing teardown")
    _driver.quit()


@fixture
def pages(driver):
    class Pages:
        loginpage = LoginPage(driver)  #creating objects of POM and passing driver
        createAccount = TestAccount(driver) #creating objects of POM and passing driver
        homepage = HomePage(driver) #creating objects of POM and passing driver
        addToCart = TestAddToCart(driver)#creating objects of POM and passing driver
    return Pages()
