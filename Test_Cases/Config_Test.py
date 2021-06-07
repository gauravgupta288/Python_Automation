from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.chrome("Drivers/chromedriver")
    return driver
