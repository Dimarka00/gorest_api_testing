from enum import Enum


class APIRoutes(str, Enum):
    USERS = '/users'

    def __str__(self) -> str:
        return self.value
