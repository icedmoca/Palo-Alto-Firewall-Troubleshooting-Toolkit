# Troubleshooting Guide

## Step-by-Step Troubleshooting

1. **Check Interface Status**
   - Use the `check_interface_status.sh` script to verify the status of all interfaces.
     ```bash
     ./scripts/connectivity_tests/check_interface_status.sh
     ```

2. **Test Network Connectivity**
   - Use the `test_ping.sh` script to ping a known IP address and check connectivity.
     ```bash
     ./scripts/connectivity_tests/test_ping.sh <IP_ADDRESS>
     ```

3. **Perform a Traceroute**
   - Use the `trace_route.sh` script to perform a traceroute to a destination IP.
     ```bash
     ./scripts/connectivity_tests/trace_route.sh <IP_ADDRESS>
     ```

4. **Analyze Logs**
   - Use the `parse_logs.py` and `identify_anomalies.py` scripts in the `log_analysis` directory to parse and analyze firewall logs.

5. **Check Performance Metrics**
   - Use the scripts in the `performance` directory to check CPU, memory usage, and run bandwidth tests.

6. **Validate Configuration**
   - Use the `config_validation` scripts to validate NAT rules, security policies, and check for duplicate objects.
