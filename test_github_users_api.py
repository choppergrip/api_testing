from fixtures.user.model import UserModel

TEST_USER = UserModel(login='6wl',
                      name='Gregory Loscombe',
                      id=15330,
                      location='Manchester',
                      public_repos=6,
                      public_gists=11,
                      followers=16,
                      following=29)

SERVER_NAME = 'GitHub.com'
JSON_CONTENT_TYPE = 'application/json; charset=utf-8'


class TestGithubUsersAPI:
    def test_get_user_info(self, app):
        """
        1. Try to get user info
        2. Check that status code is 200
        3. Check response headers
        4. Check response body
        """
        response = app.user.get_user_info(user_name=TEST_USER.login)

        assert response.status_code == 200, 'Status code is not correct'
        assert response.headers.get('Content-Type') == JSON_CONTENT_TYPE, 'Content-Type is not correct'
        assert response.headers.get('server') == SERVER_NAME, 'Server name is not correct'

        assert response.data == TEST_USER, 'User info is not correct'



# class TestGithubUsersUI:
#     pass
