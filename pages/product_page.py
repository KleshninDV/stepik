from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    button_add_to_basket = (By.CSS_SELECTOR, ".btn-add-to-basket")
    success_message = (By.CSS_SELECTOR, ".alertinner strong")
    basket_total = (By.CSS_SELECTOR, ".basket-mini .price_color")
    product_name = (By.CSS_SELECTOR, ".product_main h1")
    product_price = (By.CSS_SELECTOR, ".product_main .price_color")

    def add_product_to_basket(self):
        self.browser.find_element(*self.button_add_to_basket).click()

    def get_product_name(self):
        return self.browser.find_element(*self.product_name).text

    def get_product_price(self):
        return self.browser.find_element(*self.product_price).text

    def should_be_success_message(self, product_name):
        message = self.browser.find_element(*self.success_message).text
        assert product_name in message

    def should_be_basket_total_equal_product_price(self, product_price):
        basket_price = self.browser.find_element(
            *self.basket_total
        ).get_attribute("textContent").strip()

        basket_price = basket_price.replace("\xa0", " ")

        assert product_price == basket_price