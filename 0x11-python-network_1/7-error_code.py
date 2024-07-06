#!/usr/bin/python3
"""
This module sends a request to a URL and displays the body of the response.
If the HTTP status code is >= 400, it prints the error code.
"""

import requests
import sys


def fetch_url(url):
    """
    Sends a request to the given URL and prints the body of the response.
    If the HTTP status code is >= 400, prints the error code.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
