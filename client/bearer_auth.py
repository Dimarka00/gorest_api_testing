import os

from dotenv import load_dotenv


class BearerAuth:
    """
    Getting a token from an environment variable and adding it
    to the Authorization header of the request
    """
    load_dotenv()
    bearer_token = os.getenv('BEARER_TOKEN')

    def __call__(self, request):
        request.headers["Authorization"] = "Bearer " + self.bearer_token
        return request
