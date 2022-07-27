from requests import Response
from constants.api_endpoints import USERS_ENDPOINT
from fixtures.user.model import UserModel
from fixtures.validator import Validator


class User(Validator):
    def __init__(self, api):
        self.api = api

    def get_user_info(self, user_name: str, headers=None, response_data_model=UserModel) -> Response:
        response = self.api.client.request(
            method="GET",
            url=f'{self.api.api_url}{USERS_ENDPOINT}{user_name}',
            headers=headers,
        )
        return self.structure_response(response=response, response_data_model=response_data_model)
