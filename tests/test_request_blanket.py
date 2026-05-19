import data
from pages import UrbanRoutesPage


def test_request_blanket(driver):

    driver.get(data.URBAN_ROUTES_URL)

    page = UrbanRoutesPage(driver)

    page.set_route()
    page.call_taxi()
    page.select_comfort()
    page.request_blanket()

    assert page.blanket_enabled()