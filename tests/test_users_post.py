import allure
import pytest

from base.api.users_client import UsersClient
from models.users import CreateUser, DefaultUser
from utils.assertions.api.users_assertions import assert_user, assert_response_text
from utils.assertions.assertions_functions import assert_status_code
from utils.assertions.validate_schema import validate_schema


@pytest.mark.users
@allure.feature('Users')
@allure.story('Users API')
class TestPostUser:
    @allure.title('[POST /users] Create a new user with valid body')
    def test_post_user_with_valid_body(self, class_users_client: UsersClient):
        """
        Create a new user with valid body
        POST /users
        """
        payload = CreateUser()

        response = class_users_client.post_user_api(payload)
        json_response = response.json()

        assert_status_code(response, 201)
        assert_user(
            expected_user=json_response,
            actual_user=payload
        )

        validate_schema(
            json_response, DefaultUser.model_json_schema()
        )

    @allure.title('[POST /users] Create a new user with invalid body')
    def test_post_user_with_invalid_json(self, class_users_client: UsersClient):
        """
        Create a new user with empty body
        POST /users
        """
        response = class_users_client.post_user_api(payload={"name": ","})

        assert_status_code(response, 422)
        assert_response_text(response, 'unprocessable_entity_without_name')

    @allure.title('[POST /users] Create a new user with empty body')
    def test_post_user_with_empty_body(self, class_users_client: UsersClient):
        """
        Create a new user with empty body
        POST /users
        """
        response = class_users_client.post_user_api(payload={})

        assert_status_code(response, 422)
        assert_response_text(response, 'unprocessable_entity')
