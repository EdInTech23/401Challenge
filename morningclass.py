# Define the filename for warning logs
warning_file = 'warnings.log'
# Define the filename for error logs
error_file = 'errors.log'
# Define the filename for threat logs
threat_file = 'threats.log'

# Open the source log file in read mode
with open('source_log.log', 'r') as source_file:
    # Iterate over each line in the source log file
    for line in source_file:
        # Check if the line contains the word "WARNING"
        if 'WARNING' in line:
            # Open the warnings log file in append mode and write the line
            with open(warning_file, 'a') as file:
                file.write(line)
        # Check if the line contains the word "ERROR"
        elif 'ERROR' in line:
            # Open the errors log file in append mode and write the line
            with open(error_file, 'a') as file:
                file.write(line)
        # Check if the line contains the word "THREAT"
        elif 'THREAT' in line:
            # Open the threats log file in append mode and write the line
            with open(threat_file, 'a') as file:
                file.write(line)
