from typing import Union

import allure
from requests import Response

from client.base_client import APIClient
from client.bearer_auth import BearerAuth
from models.users import DefaultUser, CreateUser, UpdateUser
from utils.attach_api_response_to_test import attach_response
from utils.constants.routes import APIRoutes


class UsersClient(APIClient):
    @allure.step('Getting all users')
    def get_all_users_api(self, *user_id) -> Response:
        response = self.client.request('GET', APIRoutes.USERS,
                                       params={'id': user_id} if user_id else None,
                                       auth=BearerAuth())
        attach_response(response.json())
        return response

    @allure.step('Getting user with id {user_id}')
    def get_user_by_id_api(self, user_id: Union[int, str]):
        response = self.client.request('GET', f'{APIRoutes.USERS}/{user_id}',
                                       auth=BearerAuth())
        attach_response(response.json())
        return response

    @allure.step('Creating a new user')
    def post_user_api(self, payload: CreateUser):
        response = self.client.request('POST', APIRoutes.USERS,
                                       json=payload.model_dump(by_alias=True),
                                       auth=BearerAuth())
        attach_response(response.json())
        return response

    @allure.step('Updating user with id {user_id}')
    def update_user_api(self, user_id: int, payload: UpdateUser):
        return self.client.request('PUT', f'{APIRoutes.USERS}/{user_id}',
                                   json=payload.model_dump(by_alias=True),
                                   auth=BearerAuth())

    @allure.step('Deleting user with id {user_id}')
    def delete_user_api(self, user_id: int):
        return self.client.request('DELETE', f'{APIRoutes.USERS}/{user_id}',
                                   auth=BearerAuth())

    def create_user(self) -> DefaultUser:
        payload = CreateUser()
        response = self.post_user_api(payload)
        attach_response(response.json())
        return DefaultUser(**response.json())
