from typing import Union

import allure

from models.users import DefaultUser, CreateUser, UpdateUser
from utils.files_utils import read_json_common_response_data


def assert_user(
        expected_user: DefaultUser,
        actual_user: Union[DefaultUser, CreateUser, UpdateUser]
):
    with allure.step(f'Checking that "User "name" {expected_user["name"]} equals to {actual_user.name}'):
        assert (expected_user["name"]) == actual_user.name

    with allure.step(f'Checking that "User email" {expected_user["email"]} equals to {actual_user.email}'):
        assert (expected_user["email"]) == actual_user.email

    with allure.step(f'Checking that "User gender" {expected_user["gender"]} equals to {actual_user.gender}'):
        assert (expected_user["gender"]) == actual_user.gender

    with allure.step(f'Checking that "User status" {expected_user["status"]} equals to {actual_user.status}'):
        assert (expected_user["status"]) == actual_user.status


def assert_not_found(response):
    with allure.step(f'Checking that server response is 404 Not Found '):
        expected_json = read_json_common_response_data('resource_not_found')
        assert response.json() == expected_json


def assert_empty_list(response):
    with allure.step(f'Checking that server response is empty'):
        assert response.json() == []


def assert_response_id_equals_to_expected_id(response, json):
    with allure.step(f'Checking that id {response.json()[0]["id"]} in response '
                     f'equals to expected id {json["id"]} in the created object'):
        assert response.json()[0]['id'] == json['id']
