from requests import Response
from fixtures.user.model import UserModel
from fixtures.validator import Validator


class User(Validator):
    def __init__(self, app):
        self.app = app

    USER_INFO_ENDPOINT = '/users/'

    def get_user_info(self, user_name: str, headers=None, response_data_model=UserModel) -> Response:
        response = self.app.client.request(
            method="GET",
            url=f'{self.app.base_url}{self.USER_INFO_ENDPOINT}{user_name}',
            headers=headers,
        )
        return self.structure_response(response=response, response_data_model=response_data_model)
