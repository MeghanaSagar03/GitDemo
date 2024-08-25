from Utilities.lib import SeleniumWrapper
from time import sleep


class AddToCart:
    add_product = ("class","btn btn-primary")

    def __init__(self, driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def add_product(self):
        self.wrapper.click_element(self.add_product)
        sleep(10)