import requests
from .exceptions import ClientError, ServerError


def get_response_error(response):
    if 399 < response.status_code < 500:
        raise ClientError(response)
    elif 499 < response.status_code < 600:
        raise ServerError(response)


def strip_html_tags(i_string):
    """
    Quick solution to remove html tags being returned in episode description.
    Will probably replace eventually.
    """
    strippable = ('<p>', '</p>')
    spaces = ('&nbsp;',)
    breaks = ('<br>',)

    for s in strippable:
        i_string = i_string.replace(s, '')
    for s in spaces:
        i_string = i_string.replace(s, ' ')
    for s in breaks:
        i_string = i_string.replace(s, '\n')
    return i_string
