#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <SERVER_IP>"
  exit 1
fi

server_ip=$1

echo "Testing bandwidth to $server_ip..."
iperf3 -c $server_ip
