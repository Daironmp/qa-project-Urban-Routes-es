import data
from pages import UrbanRoutesPage


def test_search_taxi(driver):

    driver.get(data.URBAN_ROUTES_URL)

    page = UrbanRoutesPage(driver)

    page.set_route()
    page.call_taxi()
    page.select_comfort()
    page.add_phone()
    page.add_card()
    page.write_message()
    page.request_blanket()
    page.add_ice_cream()
    page.order_taxi()

    assert page.driver_info_visible()