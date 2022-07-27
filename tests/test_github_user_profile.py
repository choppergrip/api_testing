from constants.test_users import TEST_USER


class TestGithubUserUI:
    def test_user_profile(self, app):
        """
        1. Try to get user info via api
        2. Open user page in browser
        3. Compare data from api and UI
        """
        api_response = app.api.user.get_user_info(user_name=TEST_USER.login)

        page = app.ui.profile_page.open(username=TEST_USER.login)

        assert page.user_full_name() == api_response.data.name, 'Incorrect user name'
        assert page.user_location() == api_response.data.location, 'Incorrect user location'
        assert page.user_public_repos() == api_response.data.public_repos, 'Incorrect number of public repos'
        assert page.user_followers() == api_response.data.followers, 'Incorrect number of user followers'
        assert page.user_following() == api_response.data.following, 'Incorrect number of user following'
