#!/bin/bash
# Bash script that sends a request to url as a parameter, and displays the status code
curl -sI -w '%{response_code}' "$1" -o /dev/null
