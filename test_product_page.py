import pytest
from faker import Faker

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .config import HOST, CATALOG


def generate_links():
    links = [
        f"{CATALOG}/coders-at-work_207/?promo=offer{i}"
        for i in range(0, 10)
    ]
    links[7] = pytest.param(
        f"{CATALOG}/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail
    )
    return links


@pytest.mark.login
class TestLoginFromProductPage:
    @pytest.mark.need_review
    @pytest.mark.parametrize('link', generate_links())
    def test_guest_can_add_product_to_basket(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()
        product_page.add_to_basket(solve_quiz=True)
        product_page.should_be_added_to_basket()

    @pytest.mark.xfail(reason="created intentionally failed")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, f"{CATALOG}/coders-at-work_207/")
        product_page.open()
        product_page.add_to_basket()
        product_page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, f"{CATALOG}/coders-at-work_207/")
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.xfail(reason="created intentionally failed")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, f"{CATALOG}/coders-at-work_207/")
        product_page.open()
        product_page.add_to_basket()
        product_page.should_disappear_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        product_page = ProductPage(browser, f"{CATALOG}/the-city-and-the-stars_95/")
        product_page.open()
        product_page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser, language):
        product_page = ProductPage(browser, f"{CATALOG}/the-city-and-the-stars_95/")
        product_page.open()
        product_page.go_to_login_page(language)
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, language):
        product_page = ProductPage(browser, f"{CATALOG}/the-city-and-the-stars_95/")
        product_page.open()
        product_page.go_to_basket_page(language)
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_items()
        basket_page.should_be_empty_basket_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, f"{HOST}/accounts/login/")
        login_page.open()
        fake = Faker()
        email = fake.email()
        password = fake.password(length=10)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, f"{CATALOG}/coders-at-work_207/")
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, f"{CATALOG}/coders-at-work_207/")
        product_page.open()
        product_page.should_not_be_success_message()
        product_page.add_to_basket()
        product_page.should_be_added_to_basket()
