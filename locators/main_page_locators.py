from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_HEADER = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")

    FAQ_ROOT = (By.XPATH, "//div[@class='accordion']")

    FAQ_TITLES = {
        "price": (By.XPATH, "//div[@class='accordion']/div[1]"),
        "many_scooters": (By.XPATH, "//div[@class='accordion']/div[2]"),
        "rent_time": (By.XPATH, "//div[@class='accordion']/div[3]"),
        "rent_today": (By.XPATH, "//div[@class='accordion']/div[4]"),
        "back_early": (By.XPATH, "//div[@class='accordion']/div[5]"),
        "charger": (By.XPATH, "//div[@class='accordion']/div[6]"),
        "cancel_order": (By.XPATH, "//div[@class='accordion']/div[7]"),
        "far_from_msk": (By.XPATH, "//div[@class='accordion']/div[8]")
    }

    FAQ_ANSWERS = {
        "price": (By.XPATH, "//div[@class='accordion']/div[1]/div[@class='accordion__panel']"),
        "many_scooters": (By.XPATH, "//div[@class='accordion']/div[2]/div[@class='accordion__panel']"),
        "rent_time": (By.XPATH, "//div[@class='accordion']/div[3]/div[@class='accordion__panel']"),
        "rent_today": (By.XPATH, "//div[@class='accordion']/div[4]/div[@class='accordion__panel']"),
        "back_early": (By.XPATH, "//div[@class='accordion']/div[5]/div[@class='accordion__panel']"),
        "charger": (By.XPATH, "//div[@class='accordion']/div[6]/div[@class='accordion__panel']"),
        "cancel_order": (By.XPATH, "//div[@class='accordion']/div[7]/div[@class='accordion__panel']"),
        "far_from_msk": (By.XPATH, "//div[@class='accordion']/div[8]/div[@class='accordion__panel']")
    }

    ORDER_BUTTON_SCROLLED = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]")
