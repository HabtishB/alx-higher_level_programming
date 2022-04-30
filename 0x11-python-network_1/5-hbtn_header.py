#!/usr/bin/python3
""" This script takens in a url, sends a request to the url and displays
    the value of the X-request-Id variable found in the header of the
    response.
    Packages like urllib and sys must be used
    You are not allowed to import packages other than urllib and sys
    The value of the variable is different for each request
    You don't need to check qrguments passed to the script (number/type)
    You must also use a with statement
"""


if __name__ == "__main__":
    import requests
    import sys

    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
