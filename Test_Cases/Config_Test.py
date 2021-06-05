from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    return webdriver.chrome()
