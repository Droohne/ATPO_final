from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        keywords = ["empty", "пусто", "vacío", "vacía", "vide", "leer"]
        assert any(k in message.lower() for k in keywords), (
            f"Empty basket message is not presented. Got: '{message}'"
        )

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), (
            "Basket items are presented, but basket should be empty"
        )