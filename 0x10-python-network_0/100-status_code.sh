#!/bin/bash
# only 200 code
curl -s -o /dev/null -w "%{http_code}" "$1"
