#!/bin/bash
# Bash script that takes in url, sends GET request, and displays the response
curl -sfL "$1" -X GET
