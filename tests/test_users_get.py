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

    @allure.title('[GET /users] Get user by param name')
    def test_get_user_by_name(self, class_users_client: UsersClient, function_user: DefaultUser):
        """
        Get the user with the name param
        GET /users
        """
        response = class_users_client.get_all_users_api(params={'name': function_user.name})
        json_response = response.json()

        assert_status_code(response, 200)
        assert_response_equals_to_expected(response, 'name', function_user.name)

        validate_schema(json_response, DefaultUsersList.model_json_schema())

    @allure.title('[GET /users] Get user by param email')
    def test_get_user_by_email(self, class_users_client: UsersClient, function_user: DefaultUser):
        """
        Get the user with the email param
        GET /users
        """
        response = class_users_client.get_all_users_api(params={'email': function_user.email})
        json_response = response.json()

        assert_status_code(response, 200)
        assert_response_equals_to_expected(response, "email", function_user.email)

        validate_schema(json_response, DefaultUsersList.model_json_schema())

    @allure.title('[GET /users] Get user by param gender')
    def test_get_user_by_gender(self, class_users_client: UsersClient, function_user: DefaultUser):
        """
        Get the user with the gender param
        GET /users
        """
        response = class_users_client.get_all_users_api(params={'gender': function_user.gender})
        json_response = response.json()

        assert_status_code(response, 200)
        assert_response_equals_to_expected(response, "gender", function_user.gender)

        validate_schema(json_response, DefaultUsersList.model_json_schema())

    @allure.title('[GET /users] Get user by param status')
    def test_get_user_by_status(self, class_users_client: UsersClient, function_user: DefaultUser):
        """
        Get the user with the status param
        GET /users
        """
        response = class_users_client.get_all_users_api(params={'status': function_user.status})
        json_response = response.json()

        assert_status_code(response, 200)
        assert_response_equals_to_expected(response, "status", function_user.status)

        validate_schema(json_response, DefaultUsersList.model_json_schema())

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
