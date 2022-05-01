#!/bin/bash
# Bash script that sends a POST request to the passed url, and displays the response
curl -sL -H "content-type:application/json" -d @"$2" -X POST "$1"
