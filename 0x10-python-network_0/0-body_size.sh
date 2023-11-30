#!/bin/bash
# Usage: ./script.sh <URL>
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
