#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <IP_ADDRESS>"
  exit 1
fi

echo "Pinging $1..."
ping -c 4 $1
