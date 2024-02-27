import subprocess  # Import the subprocess module to execute shell commands
import re  # Import the re module for regular expression operations

# Prompt the user to input a target URL or IP address
target = input("Enter the target URL or IP address: ")

# Prompt the user to input a target port number for Netcat and Telnet
port = input("Enter the target port number: ")

# Banner grabbing using Netcat
# Construct the Netcat command as a list
nc_command = ['nc', '-v', '-n', '-w1', target, port]
# Execute the Netcat command using subprocess.Popen and capture the output
nc_result = subprocess.Popen(nc_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Read the standard output and error from the Netcat command
nc_output, nc_errors = nc_result.communicate()
# Print the results of the Netcat banner grabbing
print("\nNetcat banner grabbing result:")
print(nc_output.decode() + nc_errors.decode())

# Banner grabbing using Telnet
# Construct the Telnet command as a string, using 'echo' to send and then immediately close the connection
telnet_command = f'echo "QUIT" | telnet {target} {port}'
# Execute the Telnet command using subprocess.getoutput to capture the output
telnet_output = subprocess.getoutput(telnet_command)
# Print the results of the Telnet banner grabbing
print("\nTelnet banner grabbing result:")
print(telnet_output)

# Banner grabbing using Nmap
# Construct the Nmap command as a list, scanning for all well-known ports
nmap_command = ['nmap', '-sV', '--version-light', target]
# Execute the Nmap command using subprocess.Popen and capture the output
nmap_result = subprocess.Popen(nmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Read the standard output and error from the Nmap command
nmap_output, nmap_errors = nmap_result.communicate()
# Use regular expression to extract only the open ports and service information from Nmap's output
nmap_services = re.findall(r'(\d+/tcp\s+open\s+[^\n]+)', nmap_output.decode())
# Print the results of the Nmap banner grabbing, focusing on open ports and services
print("\nNmap banner grabbing result:")
for service in nmap_services:
    print(service)
