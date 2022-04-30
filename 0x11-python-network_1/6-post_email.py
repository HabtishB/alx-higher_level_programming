#!/usr/bin/python3
""" This script takes in a URL and an eamil sends a POST request
    to the passed URL with the email as a parameter and displays
    the body of the response (decoded in utf-8)
    The email must be sent in the email variable
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    Do need to check arguments passed to the script(number or type)
    with statement should be used
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    params = {'email': argv[2]}
    response = requests.post(argv[1], data=params)
    print(response.text)
