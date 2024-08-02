from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Clothing:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        self.product = driver.find_element(By.PARTIAL_LINK_TEXT, "Lowepro Slingshot Edge 250 AW")

    def select_product(self):
        self.product.click()

    def get_page_title(self):
        return self.driver.title

