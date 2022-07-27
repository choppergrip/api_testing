from seleniumpagefactory import PageFactory

from config import BASE_URL


class ProfilePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        'name': ('XPATH', './/span[@class="p-name vcard-fullname d-block overflow-hidden"]'),
        'location': ('XPATH', './/span[@class="p-label"]'),
        'public_repos': ('XPATH', '//*[@id="js-pjax-container"]/div[1]/div/div/div[2]/div/nav/a[2]/span'),
        'followers': ('XPATH', '(.//span[@class="text-bold color-fg-default"])[1]'),
        'following': ('XPATH', '(.//span[@class="text-bold color-fg-default"])[2]'),
    }

    def open(self, username: str):
        self.driver.get(f'{BASE_URL}/{username}')
        return self

    def user_full_name(self):
        return self.name.get_text()

    def user_location(self):
        return self.location.get_text()

    def user_public_repos(self):
        return int(self.public_repos.get_text())

    def user_followers(self):
        return int(self.followers.get_text())

    def user_following(self):
        return int(self.following.get_text())
