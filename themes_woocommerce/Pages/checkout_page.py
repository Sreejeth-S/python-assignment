from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Checkout:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        self.first_name = driver.find_element(By.ID, "billing_first_name")
        self.last_name = driver.find_element(By.ID, "billing_last_name")
        self.billing_company = driver.find_element(By.ID, "billing_company")
        self.billing_address_1 = driver.find_element(By.ID, "billing_address_1")
        self.billing_address_2 = driver.find_element(By.ID, "billing_address_2")
        self.billing_city = driver.find_element(By.ID, "billing_city")
        self.billing_state = driver.find_element(By.ID, "billing_state")
        self.billing_postcode = driver.find_element(By.ID, "billing_postcode")
        self.billing_phone = driver.find_element(By.ID, "billing_phone")
        self.billing_email = driver.find_element(By.ID, "billing_email")
        self.product_name = driver.find_element(By.XPATH, "//td[@class='product-name']")
        self.procuct_quantity = driver.find_element(By.XPATH, "//*[@class='product-quantity']")
        self.total = driver.find_element(By.XPATH, "//*[@class='order-total']")
        self.place_order = driver.find_element(By.ID, "place_order")

    def get_firstname(self, first_name):
        self.first_name.send_keys(first_name)

    def get_lastname(self, last_name):
        self.last_name.send_keys(last_name)

    def get_billing_company(self, billing_company):
        self.billing_company.send_keys(billing_company)

    def get_billing_address_1(self, billing_address_1):
        self.billing_address_1.send_keys(billing_address_1)

    def get_billing_address_2(self, billing_address_2):
        self.billing_address_2.send_keys(billing_address_2)

    def get_billing_city(self, billing_city):
        self.billing_city.send_keys(billing_city)

    def get_billing_state(self, billing_state):
        self.billing_state.send_keys(billing_state)

    def get_billing_postcode(self, billing_postcode):
        self.billing_postcode.send_keys(billing_postcode)

    def get_billing_phone(self, billing_phone):
        self.billing_phone.send_keys(billing_phone)

    def get_billing_email(self, billing_email):
        self.billing_email.send_keys(billing_email)

    def get_product_name(self):
        return self.product_name.text

    def get_procuct_quantity(self):
        return self.procuct_quantity.text

    def total_cost(self):
        return self.total.text

    def click_placeorder(self):
        return self.place_order.click()

    def payment_not_successful_alert(self):
        return self.driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']").text
