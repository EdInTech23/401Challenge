import zipfile

def brute_force_zip(zipfile_path, password_list_path):
    # Open the ZIP file using zipfile.ZipFile
    # zipfile_path is the path to the ZIP file you want to crack
    zip_file = zipfile.ZipFile(zipfile_path)
    
    # Open the password list file in read mode
    # password_list_path is the path to the file containing possible passwords, such as RockYou.txt
    with open(password_list_path, 'r', encoding='latin-1') as password_list:
        # Iterate over each line in the password list
        for line in password_list:
            # Strip the newline character from the end of each password
            password = line.strip('\n')
            try:
                # Try to extract the ZIP file using the current password
                # The pwd parameter takes the password as bytes, hence the conversion
                zip_file.extractall(pwd=bytes(password, 'utf-8'))
                # If the above line doesn't raise an exception, the password is correct
                print(f"Success! The password is: {password}")
                # Return the successful password and exit the function
                return password
            except:
                # If an exception is raised during the extractall call, it means the password was incorrect
                # The loop continues to the next password in the list
                continue
    
    # If the loop completes without returning, no password was found
    print("Password not found in the list.")
    return None

# Replace 'your_target_zip_file.zip' with the actual path to your ZIP file
zipfile_path = 'your_target_zip_file.zip'
# Replace 'RockYou.txt' with the path to your password list, ensuring it's the correct path to RockYou.txt
password_list_path = 'RockYou.txt'

# Call the brute force function to start the attack
brute_force_zip(zipfile_path, password_list_path)
