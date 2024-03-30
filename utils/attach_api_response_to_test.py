import allure
import json
from allure_commons.types import AttachmentType

from utils.files_utils import read_json_common_response_data


def attach_response(response):
    response = json.dumps(response, indent=4)
    allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)


def attach_expected_json(expected_json_filename):
    expected_json = read_json_common_response_data(expected_json_filename)
    expected_json = json.dumps(expected_json, indent=4)
    allure.attach(body=expected_json, name="Expected JSON", attachment_type=AttachmentType.JSON)
