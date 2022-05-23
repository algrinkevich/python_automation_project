import time
import pytest

from .pages.product_page import ProductPage


def generate_links():
    links = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(0, 10)]
    links[7] = pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)
    return links


@pytest.mark.parametrize('link', generate_links())
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_be_added_to_basket()

