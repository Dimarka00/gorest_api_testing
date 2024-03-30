import json
from typing import Union, Dict

import allure

from conftest import function_user
from models.users import DefaultUser, CreateUser, UpdateUser
from utils.attach_api_response_to_test import attach_expected_json
from utils.files_utils import read_json_common_response_data


def assert_user(
        expected_user: DefaultUser,
        actual_user: Union[DefaultUser, CreateUser, UpdateUser]):
    with allure.step(f'Checking that expected "User "name" {expected_user["name"]} in response '
                     f'equals to actual {actual_user.name} in payload'):
        assert (expected_user["name"]) == actual_user.name

    with allure.step(f'Checking that expected "User email" {expected_user["email"]} in response '
                     f'equals to actual {actual_user.email} in payload'):
        assert (expected_user["email"]) == actual_user.email

    with allure.step(f'Checking that expected "User gender" {expected_user["gender"]} in response '
                     f'equals to actual {actual_user.gender} in payload'):
        assert (expected_user["gender"]) == actual_user.gender

    with allure.step(f'Checking that expected "User status" {expected_user["status"]} in response '
                     f'equals to {actual_user.status} in payload'):
        assert (expected_user["status"]) == actual_user.status


def assert_response_text(response, expected_json_filename):
    with allure.step(f'Checking that server response is {expected_json_filename}'):
        expected_json = read_json_common_response_data(expected_json_filename)
        attach_expected_json(expected_json_filename)
        assert response.json() == expected_json


def assert_empty_list(response):
    with allure.step(f'Checking that server response is empty'):
        assert response.json() == []


def assert_response_equals_to_expected(response, key, expected_value):
    """
    Asserts that the value corresponding to the given key in the JSON response
    matches the expected value
    :param response: the response object containing JSON data.
    :param key: the key whose corresponding value needs to be compared.
    :param expected_value: the expected value for the given key.
    :return:
    """
    with allure.step(f'Checking that {key} [{response.json()[0][key]}] in response '
                     f'equals to expected {key} [{expected_value}] in the created object'):
        assert response.json()[0][key] == expected_value
