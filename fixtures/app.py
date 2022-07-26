from fixtures.client import Client
from fixtures.user.user_api import User


class App:
    def __init__(self, base_url):
        self.base_url = base_url
        self.client = Client
        self.user = User(self)
