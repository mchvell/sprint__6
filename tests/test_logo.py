import allure


from pages.main_page import MainPage as mp
from pages.order_page import OrderPage as op
from data.data_for_tests import LogoTexts

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
        assert current_url == LogoTexts.SCOOTER_URL

    # правки после код ревью - убрал слипы, вынес управление контекстом в метод
    @allure.description("Открываем главную, переходим на страницу заказа и нажимаем на лого Яндекс")
    def test_click_on_ya_logo(self, driver):
        main_page = mp(driver)
        main_page.go_to_site()
        main_page.click_on_order_button_header()

        # инициализируем создание страницы заказа
        order_page = op(driver)
        order_page.click_on_logo(logo="yandex")
        order_page.switch_tab_focus()

        current_url = driver.current_url
        assert LogoTexts.DZEN_URL in current_url
