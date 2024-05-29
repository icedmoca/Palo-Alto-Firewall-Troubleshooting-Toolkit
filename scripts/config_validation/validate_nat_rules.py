import sys
import re

def validate_nat_rules(config_file):
    with open(config_file, 'r') as file:
        lines = file.readlines()

    nat_rules = []
    for line in lines:
        # Example regex to match NAT rule entries
        match = re.match(r'NAT_RULE\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)', line)
        if match:
            rule_name, source, destination, translated = match.groups()
            nat_rules.append({
                'rule_name': rule_name,
                'source': source,
                'destination': destination,
                'translated': translated
            })
    
    return nat_rules

def main(config_file):
    nat_rules = validate_nat_rules(config_file)
    for rule in nat_rules:
        print(f"Rule: {rule['rule_name']}, Source: {rule['source']}, Destination: {rule['destination']}, Translated: {rule['translated']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python validate_nat_rules.py <config_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    main(config_file)
