import json
import time
import data

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def retrieve_phone_code(driver):
    code = None

    for _ in range(20):
        try:
            logs = [
                log["message"]
                for log in driver.get_log("performance")
                if log.get("message")
                and "api/v1/number?number" in log.get("message")
            ]

            for log in reversed(logs):
                message_data = json.loads(log)["message"]

                body = driver.execute_cdp_cmd(
                    "Network.getResponseBody",
                    {
                        "requestId":
                        message_data["params"]["requestId"]
                    }
                )

                code = "".join(
                    [
                        x for x in body["body"]
                        if x.isdigit()
                    ]
                )

        except WebDriverException:
            time.sleep(1)
            continue

        if code:
            return code

    raise Exception("No se encontró código")


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

    # ✔ switch correcto
    BLANKET_SWITCH = (By.CSS_SELECTOR, ".r-type-switch .switch")

    ICE_CREAM_PLUS = (By.CLASS_NAME, "counter-plus")
    ORDER_BUTTON = (By.CSS_SELECTOR, ".smart-button")

    SEARCH_MODAL = (By.CLASS_NAME, "order-header")
    DRIVER_MODAL = (By.CLASS_NAME, "order-number")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def set_route(self, from_address, to_address):
        self.wait.until(
            EC.visibility_of_element_located(self.FROM_FIELD)
        ).send_keys(from_address)

        self.driver.find_element(*self.TO_FIELD).send_keys(to_address)

    def call_taxi(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CALL_TAXI_BUTTON)
        ).click()

    def select_comfort(self):
        self.wait.until(
            EC.element_to_be_clickable(self.COMFORT_TARIFF)
        ).click()

    def add_phone(self, phone):
        self.wait.until(
            EC.element_to_be_clickable(self.PHONE_BUTTON)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.PHONE_INPUT)
        ).send_keys(phone)

        self.driver.find_element(*self.NEXT_BUTTON).click()

        code = retrieve_phone_code(self.driver)

        self.wait.until(
            EC.visibility_of_element_located(self.CODE_INPUT)
        ).send_keys(code)

        self.driver.find_element(*self.CONFIRM_BUTTON).click()

    def add_card(self, number, cvv):
        self.wait.until(
            EC.element_to_be_clickable(self.PAYMENT_METHOD)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.ADD_CARD)
        ).click()

        number_input = self.wait.until(
            EC.visibility_of_element_located(self.CARD_NUMBER)
        )
        number_input.clear()
        number_input.send_keys(number)

        cvv_input = self.wait.until(
            EC.visibility_of_element_located(self.CARD_CODE)
        )
        cvv_input.clear()
        cvv_input.send_keys(cvv)

        cvv_input.send_keys(Keys.TAB)

        add_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Agregar') and not(@disabled)]")
            )
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", add_button)
        add_button.click()

        # cerrar modal correctamente
        close_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".payment-picker.open .close-button.section-close")
            )
        )

        self.driver.execute_script("arguments[0].click();", close_button)

        self.wait.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".payment-picker.open"))
        )

    def write_message(self, message):
        self.wait.until(
            EC.visibility_of_element_located(self.MESSAGE_FIELD)
        ).send_keys(message)

    def request_blanket(self):
        switch = self.wait.until(
            EC.element_to_be_clickable(self.BLANKET_SWITCH)
        )

        self.driver.execute_script("arguments[0].click();", switch)

    def add_ice_cream(self):
        plus = self.wait.until(
            EC.element_to_be_clickable(self.ICE_CREAM_PLUS)
        )
        plus.click()
        plus.click()

    def order_taxi(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ORDER_BUTTON)
        ).click()

    def is_search_modal_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_MODAL)
        ).is_displayed()

    def wait_driver_info(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.DRIVER_MODAL)
        ).is_displayed()


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):

        options = webdriver.ChromeOptions()

        options.set_capability(
            "goog:loggingPrefs",
            {
                "performance":
                "ALL"
            }
        )

        options.add_experimental_option(
            "detach",
            True
        )

        cls.driver = webdriver.Chrome(
            options=options
        )

        cls.driver.maximize_window()

        cls.driver.get(
            data.URBAN_ROUTES_URL
        )

    def test_complete_order(self):

        page = UrbanRoutesPage(
            self.driver
        )

        page.set_route(
            data.address_from,
            data.address_to
        )

        page.call_taxi()

        page.select_comfort()

        page.add_phone(
            data.phone_number
        )

        page.add_card(
            data.card_number,
            data.card_code
        )

        page.write_message(
            data.message_for_driver
        )

        page.request_blanket()

        page.add_ice_cream()

        page.order_taxi()

        assert page.is_search_modal_displayed()

        assert page.wait_driver_info()

    @classmethod
    def teardown_class(cls):
        pass