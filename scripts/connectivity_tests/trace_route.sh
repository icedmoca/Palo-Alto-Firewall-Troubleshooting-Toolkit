#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <IP_ADDRESS>"
  exit 1
fi

echo "Tracerouting to $1..."
traceroute $1
