#!/usr/bin/python3
"""
This module sends a POST request to http://0.0.0.0:5000/search_user with a
letter as
a parameter and displays the results according to the JSON response.
"""

import requests
import sys


def search_user(letter):
    """
    Sends a POST request to http://0.0.0.0:5000/search_user with the given
    letter
    as a parameter and displays the results based on the JSON response.

    Args:
        letter (str): The letter to send as the 'q' parameter.

    Returns:
        None
    """
    url = 'http://0.0.0.0:5000/search_user'
    try:
        if letter:
            data = {'q': letter}
        else:
            data = {'q': ''}
        response = requests.post(url, data=data)
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    search_user(letter)
