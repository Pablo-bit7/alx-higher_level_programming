#!/usr/bin/python3
"""
This module sends a request to a URL and displays the body of the response
(decoded in utf-8). It handles HTTPError exceptions and prints the error code.
"""

import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """
    Sends a request to the given URL and prints the body of the response.
    If an HTTPError is encountered, prints the error code.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
