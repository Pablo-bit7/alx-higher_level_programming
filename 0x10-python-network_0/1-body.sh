#!/bin/bash
# This script takes a URL and displays the body of a 200 status code response
curl -s -L -w "%{http_code}" "$1" -o response.txt | grep -q "200" && cat response.txt
