from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.quantity_field = driver.find_element(By.XPATH, "//*[@class='input-text qty text']")

    def set_quantity(self, quantity_no):
        self.quantity_field.click()
        self.quantity_field.clear()
        self.quantity_field.send_keys(quantity_no)

    def click_add_to_cart(self):
        self.driver.find_element(By.XPATH, "//button[@name='add-to-cart']").click()

    def get_page_title(self):
        return self.driver.title

    def get_add_to_cart_alert(self):
        return self.driver.find_element(By.XPATH, "//*[@class='woocommerce-message']").text

    def click_viewcart(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "View cart").click()

    def click_Proceedtocheckout(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Proceed to checkout").click()