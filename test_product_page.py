import time
import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


def generate_links():
    links = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(0, 10)]
    links[7] = pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)
    return links


#@pytest.mark.parametrize('link', generate_links())
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    product_page.open()
    product_page.should_not_be_success_message()
    product_page.add_to_basket()
    product_page.should_be_added_to_basket()


@pytest.mark.xfail(reason="the test was created intentionally failed")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="the test was created intentionally failed")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    product_page.open()
    product_page.add_to_basket()
    product_page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/")
    product_page.open()
    product_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/")
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/")
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items()
    basket_page.should_be_empty_basket_message()


