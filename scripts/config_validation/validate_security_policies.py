import sys
import re

def validate_security_policies(config_file):
    with open(config_file, 'r') as file:
        lines = file.readlines()

    security_policies = []
    for line in lines:
        # Example regex to match security policy entries
        match = re.match(r'SECURITY_POLICY\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)', line)
        if match:
            policy_name, source, destination, action = match.groups()
            security_policies.append({
                'policy_name': policy_name,
                'source': source,
                'destination': destination,
                'action': action
            })
    
    return security_policies

def main(config_file):
    security_policies = validate_security_policies(config_file)
    for policy in security_policies:
        print(f"Policy: {policy['policy_name']}, Source: {policy['source']}, Destination: {policy['destination']}, Action: {policy['action']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python validate_security_policies.py <config_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    main(config_file)
