#!/usr/bin/env python3

# Script: Ops 401 Class 32 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 5/31/23
# Purpose: Continue developing your Python malware detection tool.

# Alter your search code to recursively scan each file and folder in the user input directory path and print it to the screen.
# For each file scanned within the scope of your search directory:
# Generate the file’s MD5 hash using Hashlib.
# Assign the MD5 hash to a variable.
# Print the variable to the screen along with a timestamp, file name, file size, and complete (not symbolic) file path.


import os
import hashlib
import platform
import time

def search_files(directory):
    files_searched = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not os.path.islink(file_path):  # Exclude symbolic links
                files_searched += 1
                file_size = os.path.getsize(file_path)
                md5_hash = calculate_md5(file_path)
                timestamp = time.ctime()
                
                print("Timestamp: {}".format(timestamp))
                print("File Name: {}".format(file))
                print("File Size: {} bytes".format(file_size))
                print("File Path: {}".format(file_path))
                print("MD5 Hash: {}\n".format(md5_hash))
    
    print("\nSearch complete.")
    print("Files searched: {}".format(files_searched))

def calculate_md5(file_path):
    with open(file_path, 'rb') as file:
        hash_md5 = hashlib.md5()
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_user_input(prompt):
    if platform.system() == "Windows":
        return input(prompt)
    else:
        return input(prompt).decode('utf-8')

def main():
    search_directory = get_user_input("Enter the directory to search in: ")

    search_files(search_directory)

if __name__ == "__main__":
    main()
