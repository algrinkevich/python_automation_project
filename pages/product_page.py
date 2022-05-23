from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()
        self.solve_quiz_and_get_code()

    def should_be_added_to_basket(self):
        self.should_see_success_message()
        self.should_be_product_name_in_success_message()
        self.should_see_basket_total_message()
        self.should_be_product_cost_in_basket_message()

    def should_see_success_message(self):
        self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_TOAST)

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_product_name_in_success_message(self):
        success_message = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_TOAST
        ).text
        product_name = self.get_product_name()
        assert product_name in success_message

    def get_product_cost(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST_LABEL).text

    def should_see_basket_total_message(self):
        self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE)

    def should_be_product_cost_in_basket_message(self):
        basket_total_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        product_cost = self.get_product_cost()
        assert product_cost in basket_total_message





