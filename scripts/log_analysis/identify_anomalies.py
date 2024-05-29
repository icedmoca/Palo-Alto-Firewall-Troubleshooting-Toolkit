import sys
import re
from collections import Counter

def identify_anomalies(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()

    error_pattern = re.compile(r'\[(.*?)\] \[(ERROR|CRITICAL)\] \[(.*?)\] (.*)')
    errors = [log for log in logs if error_pattern.match(log)]

    # Counting occurrences of each error message
    error_messages = [error_pattern.match(log).group(4) for log in errors]
    error_counts = Counter(error_messages)

    return error_counts

def main(log_file):
    anomalies = identify_anomalies(log_file)
    for error, count in anomalies.items():
        print(f"{error}: {count} occurrences")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python identify_anomalies.py <log_file>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    main(log_file)
