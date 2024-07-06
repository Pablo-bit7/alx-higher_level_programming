#!/usr/bin/python3
"""
This module sends a request to a URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys


def fetch_header(url):
    """
    Sends a request to the given URL and prints the value of the X-Request-Id
    variable found in the header of the response.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_header(url)
