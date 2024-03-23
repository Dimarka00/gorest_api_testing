import allure


@allure.step('Validating status code')
def assert_status_code(response, expected_code):
    with allure.step(f'Checking that response code "{response.status_code}" equals to expected code "{expected_code}"'):
        assert response.status_code == expected_code
