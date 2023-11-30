#!/bin/bash
# Usage: ./1-body.sh <URL>
[ "$(curl -s -w '%{http_code}' "$1")" -eq 200 ] && curl -s "$1"
