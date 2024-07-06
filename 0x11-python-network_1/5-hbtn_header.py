#!/usr/bin/python3
"""
This module sends a request to a URL and displays the value of the
X-Request-Id variable found in the response header.
"""

import requests
import sys


def fetch_header(url):
    """
    Sends a request to the given URL and prints the value of the X-Request-Id
    variable found in the response header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_header(url)
