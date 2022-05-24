from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()
        #self.solve_quiz_and_get_code()

    def should_be_added_to_basket(self):
        self.should_see_success_message()
        self.should_be_product_name_in_success_message()
        self.should_see_basket_total_message()
        self.should_be_product_cost_in_basket_message()

    def should_see_success_message(self):
        self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_TOAST)

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_product_name_in_success_message(self):
        product_name_in_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_TOAST
        ).text
        product_name = self.get_product_name()
        assert product_name == product_name_in_message

    def get_product_cost(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST_LABEL).text

    def should_see_basket_total_message(self):
        self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE)

    def should_be_product_cost_in_basket_message(self):
        basket_total_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        product_cost = self.get_product_cost()
        assert product_cost in basket_total_message

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_TOAST), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_TOAST), \
            "The success message is still presented"

