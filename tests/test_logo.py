import allure


from time import sleep


from pages.main_page import MainPage as mp
from pages.order_page import OrderPage as op


class TestLogo:
    @allure.description("Открываем главную, переходим на страницу заказа и нажимаем на лого Самоката")
    def test_click_on_scooter_logo(self, driver):
        main_page = mp(driver)
        main_page.go_to_site()
        main_page.click_on_order_button_header()

        # инициализируем создание страницы заказа
        order_page = op(driver)
        order_page.click_on_logo(logo="scooter")
        current_url = driver.current_url
        assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.description("Открываем главную, переходим на страницу заказа и нажимаем на лого Яндекс")
    def test_click_on_ya_logo(self, driver):
        main_page = mp(driver)
        main_page.go_to_site()
        main_page.click_on_order_button_header()

        # инициализируем создание страницы заказа
        order_page = op(driver)
        order_page.click_on_logo(logo="yandex")
        sleep(5)
        # получаем список вкладок
        handles = driver.window_handles
        # счиьаем, что новая вкладка - последняя в списке
        driver.switch_to.window(handles[-1])

        current_url = driver.current_url
        assert "dzen.ru" in current_url
