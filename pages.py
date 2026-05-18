import data

from helpers import retrieve_phone_code

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:

    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")

    CALL_TAXI_BUTTON = (By.XPATH, "//button[text()='Pedir un taxi']")
    COMFORT_TARIFF = (By.XPATH, "//div[text()='Comfort']")

    PHONE_BUTTON = (By.CLASS_NAME, "np-button")
    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Siguiente']")
    CODE_INPUT = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirmar']")

    PAYMENT_METHOD = (By.CLASS_NAME, "pp-button")
    ADD_CARD = (By.XPATH, "//div[text()='Agregar tarjeta']")
    CARD_NUMBER = (By.ID, "number")
    CARD_CODE = (By.CSS_SELECTOR, ".card-input#code")

    MESSAGE_FIELD = (By.ID, "comment")

    BLANKET_SWITCH = (By.CSS_SELECTOR, ".r-type-switch .switch")

    ICE_CREAM_PLUS = (By.CLASS_NAME, "counter-plus")

    ORDER_BUTTON = (By.CSS_SELECTOR, ".smart-button")

    SEARCH_MODAL = (By.CLASS_NAME, "order-header")
    DRIVER_MODAL = (By.CLASS_NAME, "order-number")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def set_route(self):
        self.wait.until(
            EC.visibility_of_element_located(
                self.FROM_FIELD
            )
        ).send_keys(data.address_from)

        self.driver.find_element(
            *self.TO_FIELD
        ).send_keys(data.address_to)

    def call_taxi(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.CALL_TAXI_BUTTON
            )
        ).click()

    def select_comfort(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.COMFORT_TARIFF
            )
        ).click()

    def add_phone(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.PHONE_BUTTON
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.PHONE_INPUT
            )
        ).send_keys(data.phone_number)

        self.driver.find_element(
            *self.NEXT_BUTTON
        ).click()

        code = retrieve_phone_code(self.driver)

        self.wait.until(
            EC.visibility_of_element_located(
                self.CODE_INPUT
            )
        ).send_keys(code)

        self.driver.find_element(
            *self.CONFIRM_BUTTON
        ).click()

    def add_card(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.PAYMENT_METHOD
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_CARD
            )
        ).click()

        number_input = self.wait.until(
            EC.visibility_of_element_located(
                self.CARD_NUMBER
            )
        )

        number_input.clear()
        number_input.send_keys(
            data.card_number
        )

        cvv_input = self.wait.until(
            EC.visibility_of_element_located(
                self.CARD_CODE
            )
        )

        cvv_input.clear()
        cvv_input.send_keys(
            data.card_code
        )

        cvv_input.send_keys(Keys.TAB)

        add_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(text(),'Agregar') and not(@disabled)]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            add_button
        )

        add_button.click()

        close_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    ".payment-picker.open .close-button.section-close"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            close_button
        )

        self.wait.until(
            EC.invisibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    ".payment-picker.open"
                )
            )
        )

    def write_message(self):
        self.wait.until(
            EC.visibility_of_element_located(
                self.MESSAGE_FIELD
            )
        ).send_keys(
            data.message_for_driver
        )

    def request_blanket(self):
        switch = self.wait.until(
            EC.element_to_be_clickable(
                self.BLANKET_SWITCH
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            switch
        )

    def add_ice_cream(self):
        plus = self.wait.until(
            EC.element_to_be_clickable(
                self.ICE_CREAM_PLUS
            )
        )

        plus.click()
        plus.click()

    def order_taxi(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.ORDER_BUTTON
            )
        ).click()

    def search_modal_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_MODAL
            )
        ).is_displayed()

    def driver_info_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.DRIVER_MODAL
            )
        ).is_displayed()