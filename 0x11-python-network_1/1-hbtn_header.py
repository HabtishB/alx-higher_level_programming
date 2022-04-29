#!/usr/bin/python3
""" This script takens in a url, sends a request to the url and displays
    the value of the X-request-Id variable found in the header of the
    response.
    Packages like urllib and sys must be used
    You are not allow to import packages other than urllib and sys
    The value of the variable is different for each request
    You don't need to check qrguments passed to the script (number/type)
    You must also use a with statement
"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as r:
        head = r.headers.get('X-Request-Id')
        print(head)
