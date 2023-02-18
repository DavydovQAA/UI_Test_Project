import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


@pytest.mark.order(3)
def test_buy_product_1():
    driver = webdriver.Chrome()

    print("Start Test 1")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.product_confirmation()

    print('Finish Test 1')

    time.sleep(3)
    driver.quit()


@pytest.mark.order(1)
def test_buy_product_2():
    driver = webdriver.Chrome()

    print("Start Test 2")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.product_confirmation()

    print('Finish Test 2')

    time.sleep(3)
    driver.quit()


@pytest.mark.order(2)
def test_buy_product_3():
    driver = webdriver.Chrome()

    print("Start Test 3")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.product_confirmation()

    print('Finish Test 3')

    time.sleep(3)
    driver.quit()
