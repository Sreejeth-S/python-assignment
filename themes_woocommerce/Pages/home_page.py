from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        self.clothing = driver.find_element(By.XPATH, "(//*[@class='woocommerce-loop-category__title'])[1]")
        self.dismissbutton = driver.find_element(By.XPATH, "//*[@class='woocommerce-store-notice__dismiss-link']")

    def click_clothing(self):
        self.dismissbutton.click()
        self.clothing.click()

    def get_page_title(self):
        return self.driver.title
