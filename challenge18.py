#!/usr/bin/env python3

# Script: Ops 401 Class 18 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 5/10/23
# Purpose: In Python, create a script that prompts the user to select modes, with an added mode for .zip files. 
# Resources: In class demo, class repo, and chatgpt. 






import time
import getpass
import paramiko
import zipfile

# Define functions
def iterator():
    filepath = input("Enter your dictionary filepath: ")
    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            word = line.strip()
            print(word)
            time.sleep(1)
 
def check_password():
    filepath = input("Enter the path to the password-protected zip file: ")
    dictionary_filepath = input("Enter your dictionary filepath: ")
    with open(dictionary_filepath, encoding="ISO-8859-1") as file:
        for line in file:
            password = line.strip()
            print(f"Trying password: {password}")
            try:
                with zipfile.ZipFile(filepath) as zf:
                    zf.extractall(pwd=password.encode())
                    print("Password found:", password)
                    return
            except:
                pass
    print("Password not found.")

# Main
while True:
    mode = input("""
    Brute Force Wordlist Attack Tool Menu
    1 - Offensive, Dictionary Iterator
    2 - Brute Force Password Attack (ZIP)
    3 - SSH Authentication
    4 - Exit
    Please enter a number: 
    """)
    if mode == "1":
        iterator()
    elif mode == "2":
        check_password()
    elif mode == "3":
        ssh_authentication()
    elif mode == "4":
        break
    else:
        print("Invalid selection.")
