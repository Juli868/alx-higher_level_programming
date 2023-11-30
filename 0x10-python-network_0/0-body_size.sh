#!/bin/bash
#finding the dize of the body of a website
curl -sI "$1"|grep -i Content-Length | awk'{print $2}'
