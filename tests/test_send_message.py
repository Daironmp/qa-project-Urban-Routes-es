import data
from pages import UrbanRoutesPage


def test_send_message(driver):

    driver.get(data.URBAN_ROUTES_URL)

    page = UrbanRoutesPage(driver)

    page.set_route()
    page.call_taxi()
    page.select_comfort()
    page.write_message()

    assert page.message_added()