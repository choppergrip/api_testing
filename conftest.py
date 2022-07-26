import pytest
from config import BASE_URL
from fixtures.app import App


@pytest.fixture(scope="session")
def app():
    return App(BASE_URL)

