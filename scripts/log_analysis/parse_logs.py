import sys
import re

def parse_logs(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()

    parsed_logs = []
    for log in logs:
        # Example regex to parse log entries
        match = re.match(r'\[(.*?)\] \[(.*?)\] \[(.*?)\] (.*)', log)
        if match:
            timestamp, log_level, source, message = match.groups()
            parsed_logs.append({
                'timestamp': timestamp,
                'log_level': log_level,
                'source': source,
                'message': message
            })
    
    return parsed_logs

def main(log_file):
    parsed_logs = parse_logs(log_file)
    for log in parsed_logs:
        print(log)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python parse_logs.py <log_file>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    main(log_file)
