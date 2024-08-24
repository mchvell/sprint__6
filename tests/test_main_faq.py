from pages.main_page import MainPage


class TestMainPageFaq:
    faq_answers = {
        "price": "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "many_scooters": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "rent_time": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "rent_today": "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "back_early": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "charger": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "cancel_order": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "far_from_msk": "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    }

    def test_main_page_faq_price(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.scroll_into_element(main_page.faq_root)
        main_page.set_faq_section("price")
        faq_text = self.faq_answers.get("price")
        assert faq_text == main_page.get_faq_answer("price")

    def test_main_page_faq_many_scooters(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.scroll_into_element(main_page.faq_root)
        main_page.set_faq_section("many_scooters")
        faq_text = self.faq_answers.get("many_scooters")
        assert faq_text == main_page.get_faq_answer("many_scooters")

    def test_main_page_faq_rent_time(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.scroll_into_element(main_page.faq_root)
        main_page.set_faq_section("rent_time")
        faq_text = self.faq_answers.get("rent_time")
        assert faq_text == main_page.get_faq_answer("rent_time")

    def test_main_page_faq_rent_today(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.scroll_into_element(main_page.faq_root)
        main_page.set_faq_section("rent_today")
        faq_text = self.faq_answers.get("rent_today")
        assert faq_text == main_page.get_faq_answer("rent_today")

    def test_main_page_faq_back_early(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.scroll_into_element(main_page.faq_root)
        main_page.set_faq_section("back_early")
        faq_text = self.faq_answers.get("back_early")
        assert faq_text == main_page.get_faq_answer("back_early")

    def test_main_page_faq_back_charger(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.scroll_into_element(main_page.faq_root)
        main_page.set_faq_section("charger")
        faq_text = self.faq_answers.get("charger")
        assert faq_text == main_page.get_faq_answer("charger")

    def test_main_page_faq_cancel_order(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.scroll_into_element(main_page.faq_root)
        main_page.set_faq_section("cancel_order")
        faq_text = self.faq_answers.get("cancel_order")
        assert faq_text == main_page.get_faq_answer("cancel_order")

    def test_main_page_faq_far_from_msk(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.scroll_into_element(main_page.faq_root)
        main_page.set_faq_section("far_from_msk")
        faq_text = self.faq_answers.get("far_from_msk")
        assert faq_text == main_page.get_faq_answer("far_from_msk")



