#!/bin/bash

echo "Checking CPU usage..."
top -bn1 | grep "Cpu(s)"
