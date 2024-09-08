import pytest


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

    @pytest.mark.parametrize("faq_section", faq_answers.keys())
    def test_main_page_faq(self, driver, faq_section):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.scroll_into_element(main_page.faq_root)
        main_page.set_faq_section(faq_section)
        faq_text = self.faq_answers.get(faq_section)
        assert faq_text == main_page.get_faq_answer(faq_section)


