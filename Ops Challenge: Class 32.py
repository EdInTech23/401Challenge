# Import necessary modules
import hashlib  # For generating MD5 hash
import os  # For navigating the file system
from datetime import datetime  # For timestamping

# Define a function to compute MD5 hash of a given file
def md5_hash(file_path):
    """Compute MD5 hash of a file."""
    hash_md5 = hashlib.md5()  # Create an MD5 hash object
    with open(file_path, "rb") as f:  # Open file in binary read mode
        for chunk in iter(lambda: f.read(4096), b""):  # Read file in chunks of 4096 bytes
            hash_md5.update(chunk)  # Update the hash with the chunk
    return hash_md5.hexdigest()  # Return the hexadecimal digest of the hash

# Define a function to recursively scan directories and files
def scan_directory(directory):
    """Recursively scan each file in directory and print details."""
    for root, dirs, files in os.walk(directory):  # os.walk generates the file names in a directory tree
        for name in files:  # Loop through each file in files list
            file_path = os.path.join(root, name)  # Join root path and file name to get full path
            try:
                hash_value = md5_hash(file_path)  # Compute MD5 hash for the file
                file_size = os.path.getsize(file_path)  # Get file size
                # Print file details including timestamp, name, size, MD5 hash, and full path
                print(f"Timestamp: {datetime.now()}, File Name: {name}, File Size: {file_size} bytes, MD5: {hash_value}, Path: {os.path.abspath(file_path)}")
            except Exception as e:  # Catch and print any errors encountered
                print(f"Error processing file {file_path}: {e}")

# Check if the script is run directly (not imported)
if __name__ == "__main__":
    directory_path = input("Enter the directory path to scan: ")  # Prompt user to enter directory path
    scan_directory(directory_path)  # Call the scan_directory function with the user-provided path
