import allure
import pytest

from base.api.users_client import UsersClient
from models.users import DefaultUsersList, CreateUser
from utils.assertions.api.users_assertions import assert_empty_list, assert_response_id_equals_to_expected_id
from utils.assertions.assertions_functions import assert_status_code
from utils.assertions.validate_schema import validate_schema


@pytest.mark.questions
@allure.feature('Users')
@allure.story('Users API')
class TestGetUser:
    @allure.title('Get list of all users')
    def test_get_all_users(self, class_users_client: UsersClient):
        """
        Get list of all users with default params
        GET /users
        """
        response = class_users_client.get_all_users_api()
        json_response = response.json()

        assert_status_code(response, 200)
        validate_schema(
            json_response, DefaultUsersList.model_json_schema()
        )

    @allure.title('Get user by id')
    def test_get_user_by_id(self, class_users_client: UsersClient):
        """
        Create and get a user with the id param
        GET /users
        """
        payload = CreateUser()
        create_user_response = class_users_client.post_user_api(payload)
        create_user_json = create_user_response.json()

        assert_status_code(create_user_response, 201)

        response = class_users_client.get_all_users_api(create_user_json['id'])
        json_response = response.json()

        assert_status_code(response, 200)
        assert_response_id_equals_to_expected_id(response, create_user_json)

        validate_schema(json_response, DefaultUsersList.model_json_schema())

    @pytest.mark.parametrize('user_id', [8976858695, 457364346, -1341355])
    @allure.title('Get user by not existing id')
    def test_get_user_not_exist_id(self, class_users_client: UsersClient, user_id):
        """
        Get user with the not existing id param
        GET /users
        """
        response = class_users_client.get_all_users_api(user_id)

        assert_status_code(response, 200)
        assert_empty_list(response)

    @pytest.mark.parametrize('user_id', ['fjkfdgjkdl', 'k4j5k32', 'jfjk1uf__)2'])
    @allure.title('Get user by invalid id')
    def test_get_user_invalid_id(self, class_users_client: UsersClient, user_id):
        """
        Get user with the invalid id param
        GET /users
        """
        response = class_users_client.get_all_users_api(user_id)

        assert_status_code(response, 200)
        assert_empty_list(response)

