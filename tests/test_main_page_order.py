from pages.main_page import MainPage as mp
from pages.order_page import OrderPage as op


class TestMainPageOrder:
    def test_order_with_scroll(self, driver):
        # открываем главную и скролим до кнопки Заказа
        main_page = mp(driver)
        main_page.go_to_site()
        main_page.scroll_into_element(main_page.order_button_scrolled)
        main_page.click_on_order_button_scrolled()

        # инициализируем создание страницы заказа
        order_page = op(driver)
        order_page.fill_the_form(name="Максим",
                                 surname="Птицедов",
                                 address_line="Колотушкина 10",
                                 phone_number="88005553535")

        order_page.click_on_metro(metro="Сокольники")
        order_page.click(order_page.next_button)

        # переходим на прододолжение страницы
        order_page.fill_comment_for_courier(comment="До Ре Ми Фа Со Ля Си")
        order_page.click_on_weekday(weekday="027")
        order_page.set_colour(colour="black")
        order_page.click(order_page.rent_field)
        order_page.set_rent_period(period="one_day")
        order_page.finish_order()
        order_page.click_on_modal_button(button="yes")
        order_complete_button = "Посмотреть статус"
        assert order_complete_button in order_page.get_modal_check_state()

    def test_order_with_header(self, driver):
        main_page = mp(driver)
        main_page.go_to_site()
        main_page.click_on_order_button_header()

        # инициализируем создание страницы заказа
        order_page = op(driver)
        order_page.fill_the_form(name="Билли",
                                 surname="Херрингтон",
                                 address_line="Гачимучева 10",
                                 phone_number="89119275671")

        order_page.click_on_metro(metro="Медведково")
        order_page.click(order_page.next_button)

        # переходим на прододолжение страницы
        order_page.fill_comment_for_courier(comment="Выход через сувенирную лавку")
        order_page.click_on_weekday(weekday="028")
        order_page.set_colour(colour="grey")
        order_page.click(order_page.rent_field)
        order_page.set_rent_period(period="one_day")
        order_page.finish_order()
        order_page.click_on_modal_button(button="yes")
        order_complete_button = "Посмотреть статус"
        assert order_complete_button in order_page.get_modal_check_state()


