import data

from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):

        options = webdriver.ChromeOptions()

        options.set_capability(
            "goog:loggingPrefs",
            {"performance": "ALL"}
        )

        cls.driver = webdriver.Chrome(
            options=options
        )

        cls.driver.maximize_window()

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)

    # 1
    def test_set_route(self):
        self.page.set_route()

        assert True

    # 2
    def test_select_comfort(self):
        self.page.set_route()
        self.page.call_taxi()
        self.page.select_comfort()

        assert True

    # 3
    def test_add_phone(self):
        self.page.set_route()
        self.page.call_taxi()
        self.page.select_comfort()
        self.page.add_phone()

        assert True

    # 4
    def test_add_card(self):
        self.page.set_route()
        self.page.call_taxi()
        self.page.select_comfort()
        self.page.add_phone()
        self.page.add_card()

        assert True

    # 5
    def test_confirm_code(self):
        self.page.set_route()
        self.page.call_taxi()
        self.page.select_comfort()
        self.page.add_phone()

        assert True

    # 6
    def test_send_message_driver(self):
        self.page.set_route()
        self.page.call_taxi()
        self.page.select_comfort()
        self.page.write_message()

        assert True

    # 7
    def test_request_blanket(self):
        self.page.set_route()
        self.page.call_taxi()
        self.page.select_comfort()
        self.page.request_blanket()

        assert True

    # 8
    def test_order_two_ice_creams(self):
        self.page.set_route()
        self.page.call_taxi()
        self.page.select_comfort()
        self.page.add_ice_cream()

        assert True

    # 9
    def test_search_taxi_modal(self):
        self.page.set_route()

        self.page.call_taxi()

        self.page.select_comfort()

        self.page.add_phone()

        self.page.add_card()

        self.page.write_message()

        self.page.request_blanket()

        self.page.add_ice_cream()

        self.page.order_taxi()

        assert self.page.search_modal_visible()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()