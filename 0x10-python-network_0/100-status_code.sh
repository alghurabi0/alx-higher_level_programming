#!/bin/bash
# only 200 code
curl -sLw "%{http_code}" -o /dev/null "$1"
