#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status
using urllib and displays the response in a specified format.
"""

import urllib.request


def fetch_status(url):
    """
    Fetches the status of the given URL and prints the response details.

    Args:
        url (str): The URL to fetch the status from.

    Returns:
        None
    """
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_status(url)
