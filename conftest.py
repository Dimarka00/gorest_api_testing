import pytest

from base.api.users_client import UsersClient
from client.base_client import get_http_client
from models.users import DefaultUser


@pytest.fixture(scope='class')
def class_users_client() -> UsersClient:
    client = get_http_client()
    return UsersClient(client=client)


@pytest.fixture(scope='function')
def function_user(class_users_client: UsersClient) -> DefaultUser:
    user = class_users_client.create_user()
    yield user
    class_users_client.delete_user_api(user.id)