from typing import Union, Dict

import allure
from requests import Response

from client.base_client import APIClient
from client.bearer_auth import BearerAuth
from models.users import DefaultUser, CreateUser, UpdateUser
from utils.attach_api_response_to_test import attach_response
from utils.constants.routes import APIRoutes


class UsersClient(APIClient):
    @allure.step('Getting all users')
    def get_all_users_api(self, **kwargs) -> Response:
        response = self.client.request('GET', APIRoutes.USERS,
                                       auth=BearerAuth(),
                                       **kwargs)
        attach_response(response.json())
        return response

    @allure.step('Getting user with id {user_id}')
    def get_user_by_id_api(self, user_id: Union[int, str]):
        response = self.client.request('GET', f'{APIRoutes.USERS}/{user_id}',
                                       auth=BearerAuth())
        attach_response(response.json())
        return response

    @allure.step('Creating a new user')
    def post_user_api(self, payload: Union['CreateUser', Dict[str, str]]):
        if isinstance(payload, CreateUser):
            payload_dict = payload.model_dump(by_alias=True)
        elif isinstance(payload, dict):
            payload_dict = payload
        else:
            raise ValueError("Payload should be either CreateUser instance or dict")

        response = self.client.request('POST', APIRoutes.USERS,
                                       json=payload_dict,
                                       auth=BearerAuth())
        attach_response(response.json())
        return response

    @allure.step('Updating user with id {user_id}')
    def put_user_api(self, user_id: int, payload: Union['UpdateUser', Dict[str, str]]):
        if isinstance(payload, UpdateUser):
            payload_dict = payload.model_dump(by_alias=True)
        elif isinstance(payload, dict):
            payload_dict = payload
        else:
            raise ValueError("Payload should be either UpdateUser instance or dict")
        response = self.client.request('PUT', f'{APIRoutes.USERS}/{user_id}',
                                       json=payload_dict,
                                       auth=BearerAuth())
        attach_response(response.json())
        return response

    @allure.step('Deleting user with id {user_id}')
    def delete_user_api(self, user_id: int):
        return self.client.request('DELETE', f'{APIRoutes.USERS}/{user_id}',
                                   auth=BearerAuth())

    def create_user(self) -> DefaultUser:
        payload = CreateUser()
        response = self.post_user_api(payload)
        return DefaultUser(**response.json())
