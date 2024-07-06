#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status using the requests
package and displays the body of the response in a specified format.
"""

import requests


def fetch_status(url):
    """
    Fetches the status of the given URL and prints the response details.

    Args:
        url (str): The URL to fetch the status from.

    Returns:
        None
    """
    response = requests.get(url)
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_status(url)
