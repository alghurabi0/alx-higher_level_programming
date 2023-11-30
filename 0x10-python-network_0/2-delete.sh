#!/bin/bash
# Usage: ./2-delete.sh <URL>
printf "%s" "$(curl -s -X DELETE "$1")"
