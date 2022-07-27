from fixtures.client import Client
from fixtures.user.user_api import User
from selenium import webdriver
from pages.profile_page import ProfilePage


class App:
    def __init__(self, base_url: str, api_url: str, driver: webdriver):
        self.api = API(api_url=api_url)
        self.ui = UI(base_url=base_url, driver=driver)


class API:
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.client = Client
        self.user = User(self)


class UI:
    def __init__(self, base_url: str, driver: webdriver):
        self.base_url = base_url
        self.driver = driver
        self.profile_page = ProfilePage(driver)

    def quit(self):
        self.driver.quit()
