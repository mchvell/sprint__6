from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_PERSON_ROOT = (By.XPATH, "//div[contains(@class, 'Order_Form__17u6u')]")
    INPUT_PERSON_FORM = {
        "name": (By.XPATH, "//div[contains(@class, 'Order_Form')]//input[@placeholder='* Имя']"),
        "surname": (By.XPATH, "//div[contains(@class, 'Order_Form')]//input[@placeholder='* Фамилия']"),
        "address_line": (By.XPATH, "//div[contains(@class, 'Order_Form')]//input[contains(@placeholder, 'Адрес')]"),
        "phone_number": (By.XPATH, "//div[contains(@class, 'Order_Form')]//input[contains(@placeholder, 'Телефон')]")
    }

    NEXT_BUTTON = (By.XPATH, "//div/button[text()='Далее']")

    LOGO_HEADERS = {
        "yandex": (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"),
        "scooter": (By.XPATH, "//a[contains(@class, 'LogoScooter')]")
    }

    METRO = (By.XPATH, "//div[contains(@class, 'Order_Form')]//input[@placeholder='* Станция метро']")

    DELIVERY_DATE = (By.XPATH, "//div[@class='react-datepicker__input-container']")
    DELIVERY_DATE_ROOT = (By.XPATH, "//div[@class='react-datepicker__month-container']")

    RENT_TIME = (By.XPATH, "//div[@class='Dropdown-placeholder']")

    RENT_TIME_DROPDOWN = {
        "one_day": (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"),
        "two_days": (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']"),
        "three_days": (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']"),
        "four_days": (By.XPATH, "//div[@class='Dropdown-option' and text()='четверо суток']"),
        "five_days": (By.XPATH, "//div[@class='Dropdown-option' and text()='пятеро суток']"),
        "six_days": (By.XPATH, "//div[@class='Dropdown-option' and text()='шестеро суток']"),
        "seven_days": (By.XPATH, "//div[@class='Dropdown-option' and text()='семеро суток']"),

    }

    SCOOTER_COLOURS = {
        "black": (By.XPATH, "//label/input[@id='black']"),
        "grey": (By.XPATH, "//label/input[@id='grey']")
    }

    COMMENT_FOR_COURIER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    MODAL_WINDOW_BUTTONS = {
        "yes": (By.XPATH, "//button[text()='Да']"),
        "no": (By.XPATH, "//button[text()='Нет']")
    }

    MODAL_CHECK_STATE = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Посмотреть статус']")
