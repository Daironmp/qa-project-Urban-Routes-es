import data
from pages import UrbanRoutesPage


def test_select_comfort(driver):

    driver.get(data.URBAN_ROUTES_URL)

    page = UrbanRoutesPage(driver)

    page.set_route()
    page.call_taxi()
    page.select_comfort()

    assert page.comfort_selected()