#!/usr/bin/python3
""" This script fetches https://alx-intranet.hbtn.io/status
    The package requests must be used
    You are not allowed to import packages other than request
    The body of of the response must be displayed like
      - type: <class 'str'>
      - content: OK$
"""

if __name__ == "__main__":
    import requests

    res = requests.get("https://intranet.hbtn.io/status")
    print('Body response')
    print('\t- type: {}'.format(type(res.text)))
    print('\t- content: {}'.format(type(res.text)))
