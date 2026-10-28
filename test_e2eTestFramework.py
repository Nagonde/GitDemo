import json
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects import checkout_confirmation
from pageobjects.login import LoginPage
from pageobjects.shop import Shop_Page
from pythonselenium.conftest import browserInstance

base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, ".."))  # go up one level
test_data_path = os.path.join(project_root, "data", "test_e2eTestFramework.json")

# test_data_path='../data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data=json.load(f)
    test_list=test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_items",test_list)
def test_e2e(browserInstance,test_list_items):
    driver=browserInstance
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page=LoginPage(driver)
    print(login_page.getTitle())
    shop_page=login_page.login(test_list_items["userEmail"],test_list_items["userPassword"])
    shop_page.add_products_to_cart(test_list_items["productname"])
    print(shop_page.getTitle())
    checkout_confirmation=shop_page.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()
    print(checkout_confirmation.getTitle())

# python -m pytest -n 2 -m smoke --browser_name firefox --html=rpeports/report.html
