import allure
import pytest

from base.api.users_client import UsersClient
from models.users import DefaultUser, UpdateUser
from utils.assertions.api.users_assertions import assert_user, assert_response_text
from utils.assertions.assertions_functions import assert_status_code
from utils.assertions.validate_schema import validate_schema


@pytest.mark.users
@allure.feature('Users')
@allure.story('Users API')
class TestPutUser:
    @allure.title('[PUT /users] Update a new user with valid body')
    def test_update_user_with_full_valid_body(self, class_users_client: UsersClient, function_user: DefaultUser):
        """
        Update a new user with valid body
        PUT /users
        """
        payload = UpdateUser()

        response = class_users_client.put_user_api(function_user.id, payload)
        json_response = response.json()

        assert_status_code(response, 200)
        assert_user(
            expected_user=json_response,
            actual_user=payload
        )

        validate_schema(json_response, DefaultUser.model_json_schema())

    @pytest.mark.parametrize('user_id', [743184135, -134135135, 84965396536])
    @allure.title('[PUT /users] Update a user by non existing id with empty body')
    def test_update_user_non_exist_id(self, class_users_client: UsersClient, user_id):
        """
        Update a user with by invalid id with empty body
        POST /users
        """
        payload = {}

        response = class_users_client.put_user_api(user_id, payload)

        assert_status_code(response, 404)
        assert_response_text(response, 'resource_not_found')
