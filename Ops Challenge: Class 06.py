from cryptography.fernet import Fernet
import os

# Function to generate a key for encryption/decryption
def generate_key():
    return Fernet.generate_key()

# Function to initialize Fernet with the generated key
def initialize_fernet(key):
    return Fernet(key)

# Function to encrypt a file
def encrypt_file(fernet, filepath):
    # Read the file content
    with open(filepath, 'rb') as file:
        file_data = file.read()
    
    # Encrypt the file content
    encrypted_data = fernet.encrypt(file_data)
    
    # Write the encrypted data back to the file
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)

# Function to decrypt a file
def decrypt_file(fernet, filepath):
    # Read the encrypted file content
    with open(filepath, 'rb') as file:
        encrypted_data = file.read()
    
    # Decrypt the file content
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Write the decrypted data back to the file
    with open(filepath, 'wb') as file:
        file.write(decrypted_data)

# Function to encrypt a string
def encrypt_string(fernet, text):
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text

# Function to decrypt a string
def decrypt_string(fernet, encrypted_text):
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text
from cryptography.fernet import Fernet


# Main function to handle user input and actions
def main():
    key = generate_key()
    fernet = initialize_fernet(key)

    while True:
        print("Select a mode:")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Encrypt a message")
        print("4. Decrypt a message")
        mode = input("Enter the mode (1/2/3/4): ")

        if mode == '1':
            filepath = input("Enter the path to the file to encrypt: ")
            encrypt_file(fernet, filepath)
            print("File encrypted successfully!")

        elif mode == '2':
            filepath = input("Enter the path to the file to decrypt: ")
            decrypt_file(fernet, filepath)
            print("File decrypted successfully!")

        elif mode == '3':
            text = input("Enter the message to encrypt: ")
            encrypted_text = encrypt_string(fernet, text)
            print("Encrypted message:", encrypted_text)

        elif mode == '4':
            encrypted_text = input("Enter the encrypted message: ")
            decrypted_text = decrypt_string(fernet, encrypted_text)
            print("Decrypted message:", decrypted_text)

        else:
            print("Invalid mode. Please enter a valid mode (1/2/3/4).")

if __name__ == "__main__":
    main()
