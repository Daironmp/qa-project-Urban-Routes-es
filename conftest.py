import pytest
from selenium import webdriver


@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()

    options.set_capability(
        "goog:loggingPrefs",
        {"performance": "ALL"}
    )

    driver = webdriver.Chrome(options=options)

    driver.maximize_window()

    yield driver

    driver.quit()