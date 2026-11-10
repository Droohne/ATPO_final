from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_add_to_basket_message(self, expected_name):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Success message about adding to basket is not presented"
        )
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert expected_name in message, (
            f"Product name in message does not match. "
            f"Expected: '{expected_name}', got: '{message}'"
        )

    def should_basket_total_match_price(self, expected_price):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), (
            "Basket total message is not presented"
        )
        total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert expected_price == total, (
            f"Basket total does not match product price. "
            f"Expected: '{expected_price}', got: '{total}'"
        )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Success message is presented, but should not be"
        )

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), (
            "Success message did not disappear"
        )