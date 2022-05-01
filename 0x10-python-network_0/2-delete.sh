#!/bin/bash
# Bash script that sends a delete request
curl -sfL "$1" -X DELETE
