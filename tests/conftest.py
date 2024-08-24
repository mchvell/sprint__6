import allure
import pytest
from selenium import webdriver


@allure.step("Открываем браузер Firefox")
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()