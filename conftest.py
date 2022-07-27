import pytest
from config import API_URL, BASE_URL
from fixtures.app import App
from selenium import webdriver


@pytest.fixture(scope="session")
def app():
    app = App(base_url=BASE_URL, api_url=API_URL, driver=webdriver.Chrome())
    yield app
    app.ui.quit()
