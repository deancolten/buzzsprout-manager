import requests
from .exceptions import ClientError, ServerError
import bsm.bsm


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


def convert_to_id(e_input):
    """Takes any input. If input is bsm.Episode, numeric str, or int, returns (str) episode ID"""

    if type(e_input) == bsm.Episode:
        ret_value = e_input.id

    elif isinstance(e_input, int):
        ret_value = str(e_input)

    elif isinstance(e_input, str) and e_input.isnumeric():
        ret_value = e_input
    else:
        raise TypeError(
            f"Must provide an episode object or id, either str or int.")

    return ret_value
