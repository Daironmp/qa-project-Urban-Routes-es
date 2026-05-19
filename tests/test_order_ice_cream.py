import data
from pages import UrbanRoutesPage


def test_order_two_ice_creams(driver):

    driver.get(data.URBAN_ROUTES_URL)

    page = UrbanRoutesPage(driver)

    page.set_route()
    page.call_taxi()
    page.select_comfort()
    page.add_ice_cream()

    assert page.ice_cream_added()