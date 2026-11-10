import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
LOGIN_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


@pytest.mark.need_review
@pytest.mark.parametrize("link", [
    PRODUCT_LINK + "?promo=offer0",
    PRODUCT_LINK + "?promo=offer1",
    PRODUCT_LINK + "?promo=offer2",
    PRODUCT_LINK + "?promo=offer3",
    PRODUCT_LINK + "?promo=offer4",
    PRODUCT_LINK + "?promo=offer5",
    PRODUCT_LINK + "?promo=offer6",
    pytest.param(
        PRODUCT_LINK + "?promo=offer7",
        marks=pytest.mark.xfail(reason="Known bug: wrong product name in success message"),
    ),
    PRODUCT_LINK + "?promo=offer8",
    PRODUCT_LINK + "?promo=offer9",
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    page.add_product_to_basket()
    page.should_be_add_to_basket_message(product_name)
    page.should_basket_total_match_price(product_price)


@pytest.mark.xfail(reason="Success message appears after adding product to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK + "?promo=offer0")
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Success message does not disappear after adding product to basket")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK + "?promo=offer0")
    page.open()
    page.add_product_to_basket()
    page.should_success_message_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items()
    basket_page.should_be_empty_basket_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, LOGIN_LINK)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "Test12345!"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_LINK + "?promo=offer0")
        page.open()
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        page.add_product_to_basket()
        page.should_be_add_to_basket_message(product_name)
        page.should_basket_total_match_price(product_price)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        page.should_not_be_success_message()