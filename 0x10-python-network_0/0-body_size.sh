#!/bin/bash
# Bash script that takes in url, and displays the size of the body of the
# response, in bytes using curl

curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
