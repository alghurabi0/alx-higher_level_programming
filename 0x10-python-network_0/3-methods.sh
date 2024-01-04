#!/bin/bash
# Usage: ./3-methods.sh <URL>
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d ' ' -f 2-
