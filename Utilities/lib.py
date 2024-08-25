import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from typing import Self


MAX_TIMEOUT = 10


def _wait(func):
    def wrapper(instance: Self, locator: tuple[str, str], **kwargs: dict[str, str]):
        print(f"waiting for element {locator}")
        w = WebDriverWait(instance.driver, MAX_TIMEOUT)
        v = visibility_of_element_located(locator)
        w.until(v)
        func(instance, locator, **kwargs)

    return wrapper


def __wait(cls):
    for key, value in cls.__dict__.items():
        if callable(value) and key != "__init__" and key != "page_down":
            setattr(cls, key, _wait(value))
    return cls


@__wait
class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator: tuple[str, str]):
        self.driver.find_element(*locator).click()

    def enter_text(self, locator: tuple[str, str], *, value: str):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    def select_item(self, locator: tuple[str, str], *, item: str):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(item)

    def page_down(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.PAGE_DOWN).perform()











    # def page_up(self,driver):
    #     body = driver.find_element('body')
    #     body.send_keys(Keys.PAGE_UP)
    #
    # def page_down(self,driver):
    #    body = driver.find_element('body')
    #    body.send_keys(Keys.PAGE_DOWN)
    #
    # def test_page_up_and_down(driver):
    #     time.sleep(3)
    #
    #     driver.page_down(driver)
    #     time.sleep(2)
    #     driver.page_up(driver)
    #     time.sleep(2)
    #
    #
    #




# class SeleniumWrapper:
#     def __init__(self,driver):
#         self.driver = driver
#
#     def enter_text(self, locator: tuple[str, str], *, value: str) -> None:
#
#         self.driver.find_element(*locator).clear()
#         self.driver.find_element(*locator).send_keys(value)
#
#     def click_element(self, locator: tuple[str, str]):
#         self.driver.find_element(*locator).click()
#
#     def select_item(self, locator: tuple[str, str], *, item: str):
#         element = self.driver.find_element(*locator)
#         select = Select(element)
#         select.select_by_visible_text(item)
