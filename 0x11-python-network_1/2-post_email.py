#!/usr/bin/python3
""" This script takes in a URL and an eamil sends a POST request
    to the passed URL with the email as a parameter and displays
    the body of the response (decoded in utf-8)
    The email must be sent in the email variable
    You must use the packages urllib and sys
    You are not allowed to import packages other than urllib and sys
    Do need to check arguments passed to the script(number or type)
    with statement should be used
"""

if __name__ == "__main__":
    from urllib import parse
    from urllib import request
    from sys import argv
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    req = request.Request(argv[1], data=data)
    with request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
