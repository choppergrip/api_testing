import requests
from requests import Response


class Client:
    @staticmethod
    def request(method: str, url: str, **kwargs) -> Response:
        """
        Wrapper around HTTP library for requests

        :param str method: Http method like GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE
        :param str url: Endpoint for request
        :param kwargs: Any other parameters that requests library supports
        """
        return requests.request(method, url, **kwargs)
