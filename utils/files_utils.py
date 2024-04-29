import json
import os


def get_test_data_path():
    return os.path.join(os.path.dirname(__file__), "..", "test_data")


def get_common_response_path():
    return f"{get_test_data_path()}/common/responses"


def read_json_file_data(path):
    with open(f"{path}.json", "r") as f:
        data = json.load(f)
    return data


def read_json_test_data(request):
    return read_json_file_data(f"{get_test_data_path()}/{request.node.originalname}")


def read_json_common_response_data(file_name):
    return read_json_file_data(f"{get_common_response_path()}/{file_name}")
