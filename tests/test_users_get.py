import allure
import pytest

from base.api.users_client import UsersClient
from models.users import DefaultUsersList, DefaultUser
from utils.assertions.api.users_assertions import (assert_empty_list, assert_not_found,
                                                   assert_response_equals_to_expected)
from utils.assertions.assertions_functions import assert_status_code
from utils.assertions.validate_schema import validate_schema


@pytest.mark.questions
@allure.feature('Users')
@allure.story('Users API')
class TestGetUser:
    @allure.title('[GET /users] Get list of all users')
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

    @allure.title('[GET /users] Get user with param id')
    def test_get_user_by_id(self, class_users_client: UsersClient, function_user: DefaultUser):
        """
        Create and get a user with the id param
        GET /users
        """
        response = class_users_client.get_all_users_api(params={'id': function_user.id})
        json_response = response.json()

        assert_status_code(response, 200)
        assert_response_equals_to_expected(response, "id", function_user.id)

        validate_schema(json_response, DefaultUsersList.model_json_schema())

    @pytest.mark.parametrize('user_id', [8976858695, 457364346, -1341355])
    @allure.title('[GET /users] Get user by not existing param id')
    def test_get_user_not_exist_id(self, class_users_client: UsersClient, user_id):
        """
        Get user with the not existing id param
        GET /users
        """
        response = class_users_client.get_all_users_api(params={'id': user_id})

        assert_status_code(response, 200)
        assert_empty_list(response)

    @pytest.mark.parametrize('user_id', ['fjkfdgjkdl', 'k4j5k32', 'jfjk1uf__)2'])
    @allure.title('[GET /users] Get user by invalid param id')
    def test_get_user_invalid_id(self, class_users_client: UsersClient, user_id):
        """
        Get user with the invalid id param
        GET /users
        """
        response = class_users_client.get_all_users_api(params={'id': user_id})

        assert_status_code(response, 200)
        assert_empty_list(response)

    @pytest.mark.parametrize("param_name", ["name", "email", "gender", "status"])
    @allure.title('[GET /users] Get user by param {param_name}')
    def test_get_user_by_param(self, class_users_client: UsersClient, function_user: DefaultUser, param_name):
        """
        Get the user with the specified param
        GET /users
        """
        params = {param_name: getattr(function_user, param_name)}
        response = class_users_client.get_all_users_api(params=params)
        json_response = response.json()

        assert_status_code(response, 200)
        assert_response_equals_to_expected(response, param_name, getattr(function_user, param_name))

        validate_schema(json_response, DefaultUsersList.model_json_schema())

    @allure.title('[GET /users/{id}] Get user by id')
    def test_get_user(self, class_users_client: UsersClient, function_user):
        """
        Get user by valid id
        GET /users/{users_id}
        """
        response = class_users_client.get_user_by_id_api(function_user.id)
        json_response = response.json()

        assert_status_code(response, 200)

        validate_schema(
            json_response, DefaultUser.model_json_schema()
        )

    @allure.title('[GET /users/{id}] Get user by invalid id')
    @pytest.mark.parametrize('user_id', [148148151, 753715854, -134135135])
    def test_get_user_not_exist(self, class_users_client: UsersClient, user_id):
        """
        Get user by invalid id
        GET /users/{users_id}
        """
        response = class_users_client.get_user_by_id_api(user_id)

        assert_status_code(response, 404)
        assert_not_found(response)
