import data
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    def prepare_comfort(self, driver):
        driver.get(data.URBAN_ROUTES_URL)

        page = UrbanRoutesPage(driver)

        page.set_route()
        page.call_taxi()
        page.select_comfort()

        return page

    def test_set_route(self, driver):
        driver.get(data.URBAN_ROUTES_URL)

        page = UrbanRoutesPage(driver)

        page.set_route()

        assert page.route_is_set()

    def test_select_comfort(self, driver):
        page = self.prepare_comfort(driver)

        assert page.comfort_selected()

    def test_add_phone(self, driver):
        page = self.prepare_comfort(driver)

        page.add_phone()

        assert page.phone_added()

    def test_add_card(self, driver):
        page = self.prepare_comfort(driver)

        page.add_card()

        assert page.card_added()

    def test_confirm_code(self, driver):
        page = self.prepare_comfort(driver)

        page.add_phone()

        assert page.code_confirmed()

    def test_send_message_driver(self, driver):
        page = self.prepare_comfort(driver)

        page.write_message()

        assert page.message_sent()

    def test_request_blanket(self, driver):
        page = self.prepare_comfort(driver)

        page.request_blanket()

        assert page.blanket_requested()

    def test_order_two_ice_creams(self, driver):
        page = self.prepare_comfort(driver)

        page.add_ice_cream()

        assert page.ice_cream_count() == 2

    def test_search_taxi_modal(self, driver):
        page = self.prepare_comfort(driver)

        page.add_phone()
        # page.add_card()
        page.write_message()
        page.order_taxi()

        assert page.search_modal_visible()
        assert page.driver_info_visible()