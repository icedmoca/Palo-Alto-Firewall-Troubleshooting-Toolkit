#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <output_file>"
  exit 1
fi

output_file=$1

echo "Exporting logs to $output_file..."
cp /var/log/paloalto/* $output_file
