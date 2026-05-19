import data
from pages import UrbanRoutesPage


def test_add_phone(driver):

    driver.get(data.URBAN_ROUTES_URL)

    page = UrbanRoutesPage(driver)

    page.set_route()
    page.call_taxi()
    page.select_comfort()
    page.add_phone()

    assert page.phone_added()