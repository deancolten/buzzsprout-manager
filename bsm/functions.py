import requests
from .exceptions import ClientError, ServerError


def get_response_error(response):
    if 399 < response.status_code < 500:
        raise ClientError(response)
    elif 499 < response.status_code < 600:
        raise ServerError(response)
