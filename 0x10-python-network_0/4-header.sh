#!/bin/bash
#send a rquest for a header with "X-School-User-Id" and variable 98 as a header
curl -sH "X-School-User-Id: 98" "$1"
