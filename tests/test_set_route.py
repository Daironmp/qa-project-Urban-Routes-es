import data
from pages import UrbanRoutesPage


def test_set_route(driver):

    driver.get(data.URBAN_ROUTES_URL)

    page = UrbanRoutesPage(driver)

    page.set_route()

    assert page.route_is_set()