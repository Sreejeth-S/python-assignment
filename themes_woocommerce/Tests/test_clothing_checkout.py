import time
import pytest
from selenium import webdriver
from themes_woocommerce.Pages.home_page import HomePage
from themes_woocommerce.Pages.all_clothing_page import Clothing
from themes_woocommerce.Pages.product_page import ProductPage
from themes_woocommerce.Pages.checkout_page import Checkout


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Firefox()
    driver.get("https://themes.woocommerce.com/storefront/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestClothing:

    # clicks on clothing
    def test_navigate_to_clothing(self):
        home_page = HomePage(self.driver)
        home_page.click_clothing()
        pagetitle = home_page.get_page_title()
        assert pagetitle == "Clothing – Storefront"

    # selects the product
    def test_select_product(self):
        clothing = Clothing(self.driver)
        clothing.select_product()
        pagetitle = clothing.get_page_title()
        assert pagetitle == "Lowepro Slingshot Edge 250 AW – Storefront"

    # changes the procuct quantity
    def test_change_quantity(self):
        product = ProductPage(self.driver)
        product.set_quantity("2")

    # add the procuct to cart
    def test_add_to_cart(self):
        product = ProductPage(self.driver)
        product.click_add_to_cart()
        alert = product.get_add_to_cart_alert()
        assert alert == "View cart\n2 × “Lowepro Slingshot Edge 250 AW” have been added to your cart."

    # view the cart
    def test_click_viewcart(self):
        product = ProductPage(self.driver)
        product.click_viewcart()

    # proceeds for checkout
    def test_click_Proceedtocheckout(self):
        product = ProductPage(self.driver)
        product.click_Proceedtocheckout()

    # fills all information required for checkout & also verifies the cart items and total
    def test_checkout(self):
        checkout = Checkout(self.driver)
        checkout.get_firstname("Sreejeth")
        checkout.get_lastname("S")
        checkout.get_billing_company("Trellis")
        checkout.get_billing_address_1("60th Olive Way")
        checkout.get_billing_address_2("Robert street")
        checkout.get_billing_city("Birmingham")
        checkout.get_billing_state("London")
        checkout.get_billing_postcode("B1 1BA")
        checkout.get_billing_phone("8745935672")
        checkout.get_billing_email("sreejeth@temp9977.com")

        productname = checkout.get_product_name()
        assert productname == "Lowepro Slingshot Edge 250 AW  × 2"

        productquantity = checkout.get_procuct_quantity()
        assert productquantity == "× 2"

        totalcost = checkout.total_cost()
        assert totalcost == "Total £219.90"

        time.sleep(2)
        checkout.click_placeorder()
        alert = checkout.payment_not_successful_alert()
        assert alert == "Invalid payment method."
        # Since it a demo website the payment is not working so asserted the error message instead