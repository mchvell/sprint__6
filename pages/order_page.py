import allure


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as op
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.input_root = op.INPUT_PERSON_ROOT
        self.input_form = op.INPUT_PERSON_FORM
        self.next_button = op.NEXT_BUTTON
        self.metro_input = op.METRO
        self.colour = op.SCOOTER_COLOURS
        self.period = op.RENT_TIME_DROPDOWN
        self.rent_field = op.RENT_TIME
        self.delivery_day = op.DELIVERY_DATE
        self.comment_field = op.COMMENT_FOR_COURIER
        self.order_button = op.ORDER_BUTTON
        self.modal_buttons = op.MODAL_WINDOW_BUTTONS
        self.modal_check_state = op.MODAL_CHECK_STATE
        self.logos = op.LOGO_HEADERS

    @allure.step("Заполняем форму на первой странице создания заказа")
    def fill_the_form(self, **kwargs):
        for field, value in kwargs.items():
            locator = self.input_form.get(field)
            self.find_element(locator, 10).send_keys(value)
        return self

    @allure.step("Кликаем на элемент")
    def click(self, locator):
        element = self.find_element(locator, 10)
        return element.click()

    @staticmethod
    def get_metro_station(metro):
        return By.XPATH, f"//button[starts-with(@class, 'Order_SelectOption')]/div[text()='{metro}']"

    @allure.step("Выбираем станцию метро")
    def click_on_metro(self, metro):
        self.click(self.metro_input)
        metro_locator = self.get_metro_station(metro)
        return self.find_element(metro_locator, 10).click()

    @allure.step("Выбираем цвет")
    def set_colour(self, **kwargs):
        for colour, value in kwargs.items():
            locator = self.colour.get(value)
            self.find_element(locator, 10).click()
        return self

    @allure.step("Выбираем срок аренды")
    def set_rent_period(self, **kwargs):
        for period, value in kwargs.items():
            locator = self.period.get(value)
            self.find_element(locator, 10).click()
            return self

    @staticmethod
    def get_calendar_weekday(weekday):
        return By.XPATH, f"//div[@class='react-datepicker__month-container']//div[@class='react-datepicker__day react-datepicker__day--{weekday}']"

    @allure.step("Выбираем будний день для доставки")
    def click_on_weekday(self, weekday):
        self.click(self.delivery_day)
        weekday_locator = self.get_calendar_weekday(weekday)
        return self.find_element(weekday_locator, 10).click()

    @allure.step("Заполняем комментарий для курьера")
    def fill_comment_for_courier(self, comment):
        comment_field = self.find_element(self.comment_field, 10)
        comment_field.send_keys(comment)
        return self

    @allure.step("Нажимаем на кнопку 'Заказать' в конце формы")
    def finish_order(self):
        return self.find_element(self.order_button, 10).click()

    @allure.step("Нажимаем на кнопку в модальном окне")
    def click_on_modal_button(self, **kwargs):
        for button, value in kwargs.items():
            locator = self.modal_buttons.get(value)
            self.find_element(locator, 10).click()
        return self

    @allure.step("Получаем текст кнопки 'Статус заказа' в модалке")
    def get_modal_check_state(self):
        return self.find_element(self.modal_check_state, 10).text

    @allure.step("Нажимаем на логотип")
    def click_on_logo(self, **kwargs):
        for logo, value in kwargs.items():
            logo_locator = self.logos.get(value)
            self.find_element(logo_locator, 10).click()
        return self

    @allure.step("Получаем список вкладок, ожидаем прогрузки новой вкладки")
    def switch_tab_focus(self):
        tab_list = self.driver.window_handles
        tab = self.driver.switch_to.window(tab_list[-1])

        # немного наколхозил... можно было бы сделать отдельный метода вейтов
        WebDriverWait(self.driver, 10).until(
            EC.url_changes("about:blank")
        )

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(("tag name", "body"))
        )

        return tab
