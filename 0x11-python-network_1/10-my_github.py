#!/usr/bin/python3
""" A python script that takes your github credentials (username and password)
and uses the GitHubAPI to display your id
   * Must use Basic Authentication with personal access token as poassword
    (to access information read.user permission is needed)
   * The first argument is username and the second password
   * The packages requests and sys must be used
   * Other packages are not used
   * arguments passed need not to be checked
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    response = requests.get('https://api.github.com/user',
                            auth=(argv[1], argv[2]))
    if response.status_code >= 400:
        print('None')
    else:
        print(response.json().get('id'))
