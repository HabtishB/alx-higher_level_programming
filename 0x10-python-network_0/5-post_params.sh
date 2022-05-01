#!/bin/bash
# Bash script that sends a POST request to the passed url, and displays the response
curl -sL -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
