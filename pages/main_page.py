import allure


from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as mp


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.faq_root = mp.FAQ_ROOT
        self.faq_sections = mp.FAQ_TITLES
        self.faq_answers = mp.FAQ_ANSWERS
        self.order_button_scrolled = mp.ORDER_BUTTON_SCROLLED
        self.order_button_header = mp.ORDER_BUTTON_HEADER

    @allure.step("Устанавливаем раздел FAQ")
    def set_faq_section(self, section):
        section = self.faq_sections.get(section)
        return self.find_element(section, 10).click()

    @allure.step("Скролим до нужного элемента")
    def scroll_into_element(self, element_locator):
        element = self.find_element(element_locator, 15)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получает текстовку FAQ")
    def get_faq_answer(self, answer):
        answer = self.faq_answers.get(answer)
        return self.find_element(answer, 10).text

    @allure.step("Нажимаем на кнопку 'Заказать' в середине страницы")
    def click_on_order_button_scrolled(self):
        return self.find_element(self.order_button_scrolled, 10).click()

    @allure.step("Нажимаем на кнопку 'Заказать' в верхнем навбаре")
    def click_on_order_button_header(self):
        return self.find_element(self.order_button_header, 10).click()

