import allure
import requests


class HTTPClient:
    """
    Overriding the base requests client
    """
    def __init__(self):
        self.base_url = 'https://gorest.co.in/public/v2'

    @allure.step('Making "{method}" to "{url}"')
    def request(self, method, url, **kwargs):
        """
        Overriding the logic of the request method
        with the addition of logging the request type and its URL
        :param method: HTTP method (POST, GET, etc.)
        :param url: the path where the request is sent
        """
        return requests.request(method, f"{self.base_url}{url}", **kwargs)


class APIClient:
    def __init__(self, client: HTTPClient) -> None:
        self._client = client

    @property
    def client(self) -> HTTPClient:
        return self._client


def get_http_client() -> HTTPClient:
    return HTTPClient()
