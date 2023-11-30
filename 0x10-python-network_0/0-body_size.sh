#!/usr/bin/bash
#finding the dize of the body of a website
curl -sI "$1"|wc -l | cat 
