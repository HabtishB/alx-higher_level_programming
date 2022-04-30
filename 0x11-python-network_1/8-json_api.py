#!/usr/bin/python3
"""
 Takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter
 as a parameter
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    q = argv[1] if len(argv) > 1 else ""
    res = requests.post('https://0.0.0.0:5000/search_user', data={'query': q})
    try:
        dic = res.json()
        if dic == {}:
            print('No result')
        else:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
    except ValueError:
        print('Not a valid JSON')
