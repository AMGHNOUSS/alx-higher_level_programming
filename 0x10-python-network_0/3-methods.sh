#!/bin/bash
# Take in a URL and display all HTTP methods the server will accept.
curl -sX OPTIONS "$1"
