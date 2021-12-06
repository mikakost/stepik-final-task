from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty_message_appear(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET), "Basket is empty message not appear"

    def should_be_empty_basket(self):
        assert not self.is_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), "Basket is empty"
