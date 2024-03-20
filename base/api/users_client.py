import allure
from requests import Response

from client.base_client import APIClient
from client.bearer_auth import BearerAuth
from models.users import DefaultUser, CreateUser, UpdateUser
from utils.constants.routes import APIRoutes


class UsersClient(APIClient):
    @allure.step('Getting all users')
    def get_all_users_api(self) -> Response:
        return self.client.request('GET', APIRoutes.USERS)

    @allure.step('Creating a new user')
    def post_user_api(self, payload: CreateUser):
        return self.client.request('POST', APIRoutes.USERS,
                                   json=payload.model_dump(by_alias=True),
                                   auth=BearerAuth())

    @allure.step('Updating user with id {user_id}')
    def update_user_api(self, user_id: int, payload: UpdateUser):
        return self.client.request('PUT', f'{APIRoutes.USERS}/{user_id}',
                                   json=payload.model_dump(by_alias=True),
                                   auth=BearerAuth())

    @allure.step('Deleting user with id {user_id}')
    def delete_user_api(self, user_id: int):
        return self.client.request('DELETE', f'{APIRoutes.USERS}/{user_id}')

    def create_user(self) -> DefaultUser:
        payload = CreateUser()
        response = self.post_user_api(payload)
        return DefaultUser(**response.json())

