from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_sort(browserInstance):
    driver = browserInstance
    browsersortedveggies = []
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    # click column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
    # collecting all veggies into list
    veggiewebelements = driver.find_elements(By.XPATH, "//tr/td[1]")

    for element in veggiewebelements:
        browsersortedveggies.append(element.text)

    originalbrowsersortedlist = browsersortedveggies.copy()
    # sort the browserveggieslist
    browsersortedveggies.sort()

    assert originalbrowsersortedlist == browsersortedveggies
