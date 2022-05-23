from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE_TOAST = (By.XPATH, "//div[@id='messages']/div[1]")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_TOTAL_MESSAGE = (By.XPATH, "//div[@id='messages']/div[3]")
    PRODUCT_COST_LABEL = (By.CSS_SELECTOR, "p.price_color")
