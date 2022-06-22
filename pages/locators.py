from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.NAME, "registration-email")
    PASSWORD_FIELD = (By.NAME, "registration-password1")
    REPEAT_PASSWORD_FIELD = (By.NAME, "registration-password2")
    SIGN_UP_BUTTON = (By.NAME, "registration_submit")
    SUCCESS_SIGN_UP_ALERT = (By.CLASS_NAME, "alert-success")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_SUCCESS_TOAST = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_TOTAL_MESSAGE = (By.XPATH, "//div[@id='messages']/div[3]")
    PRODUCT_COST_LABEL = (By.CSS_SELECTOR, "p.price_color")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


