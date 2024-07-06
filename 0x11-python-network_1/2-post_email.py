#!/usr/bin/python3
"""
This module sends a POST request to a URL with an email as a parameter and
displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """
    Sends a POST request to the given URL with the email as a parameter and
    prints the body of the response (decoded in utf-8).

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to send as a parameter.

    Returns:
        None
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        content = response.read().decode('utf-8')
        print(content)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
