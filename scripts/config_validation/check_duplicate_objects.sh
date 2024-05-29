#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <config_file>"
  exit 1
fi

config_file=$1

echo "Checking for duplicate objects in $config_file..."

duplicates=$(grep -oP 'OBJECT\s+\K\S+' $config_file | sort | uniq -d)

if [ -z "$duplicates" ]; then
  echo "No duplicate objects found."
else
  echo "Duplicate objects found:"
  echo "$duplicates"
fi
