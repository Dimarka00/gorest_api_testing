import allure
import pytest

from base.api.users_client import UsersClient
from models.users import CreateUser
from utils.assertions.api.users_assertions import assert_response_text
from utils.assertions.assertions_functions import assert_status_code


@pytest.mark.users
@allure.feature('Users')
@allure.story('Users API')
class TestDeleteUser:
    @allure.title('[DELETE /users] Delete user by valid id')
    def test_delete_exist_user(self, class_users_client: UsersClient):
        payload = CreateUser()
        create_user_response = class_users_client.post_user_api(payload)
        create_user_json = create_user_response.json()

        assert_status_code(create_user_response, 201)

        delete_user_response = class_users_client.delete_user_api(create_user_json['id'])
        get_user_response = class_users_client.get_user_by_id_api(create_user_json['id'])

        assert_status_code(delete_user_response, 204)
        assert_status_code(get_user_response, 404)

    @pytest.mark.parametrize('user_id', [413531513, -13453155, 35653662])
    @allure.title('[DELETE /users] Delete user by invalid id')
    def test_delete_not_exist_user(self, class_users_client: UsersClient, user_id):
        delete_user_response = class_users_client.delete_user_api(user_id)

        assert_status_code(delete_user_response, 404)
        assert_response_text(delete_user_response, 'resource_not_found')
