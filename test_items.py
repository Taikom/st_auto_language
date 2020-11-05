import pytest
from selenium import webdriver
import time

#@pytest.mark.parametrize() #
def test_add_exist(browser):
    try:
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.implicitly_wait(5)
        browser.get(link)
        assert browser.find_element_by_css_selector(".btn-add-to-basket"), "Button ADD not exist"
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

