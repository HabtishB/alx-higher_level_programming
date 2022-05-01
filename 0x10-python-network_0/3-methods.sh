#!/bin/bash
# Bash script that displays accepted HTTP methods
curl -sfL "$1" -X OPTIONS | grep -i Allow | cut -d " " -f2-
