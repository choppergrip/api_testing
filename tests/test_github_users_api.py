from constants.test_users import TEST_USER

EXPECTED_HEADERS = {
    'Server': 'GitHub.com',
    'Content-Type': 'application/json; charset=utf-8'
}


class TestGithubUsersAPI:
    def test_get_user_info(self, app):
        """
        1. Try to get user info
        2. Check that status code is 200
        3. Check response body
        4. Check response headers
        """
        response = app.api.user.get_user_info(user_name=TEST_USER.login)

        assert response.status_code == 200, 'Status code is not correct'
        assert response.data == TEST_USER, 'User info is not correct'

        for key, value in EXPECTED_HEADERS.items():
            assert response.headers.get(key) == value, f'{key} header is not correct'
