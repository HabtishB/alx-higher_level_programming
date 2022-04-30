#!/usr/bin/python3
""" This script takes in a URL and displays the body of the response
    decoded in utf-8
    You have to manage the urllib.error.HTPError eexceptions and print
    the Error code: followed by the HTTP status code
    The packages urllib and sys should be used
    You are not allowed to import packages other than urllib and sys
    Check arguments passed to the script(number or type) is not needed
    with statement should be used
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
