#!/bin/bash
# Usage: ./5-post_params.sh <URL>
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
