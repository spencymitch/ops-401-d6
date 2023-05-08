#!/usr/bin/env python3

# Script: Ops 401 Class 16 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 5/8/23
# Purpose: In Python, create a script that prompts the user to select modes.
# Resources: In class demo, class repo, and chatgpt. 


import time, getpass

# Prompt user to select mode
mode = input("Select a mode:\n1. Iterate through word list and print each word with delay.\n2. Search word list for a specific string.\n")

if mode == "1":
    # Mode 1: Iterate through word list and print each word with delay
    file_path = input("Enter word list file path:\n")
    delay = float(input("Enter delay between words (in seconds):\n"))
    
    with open(file_path) as file:
        for line in file:
            word = line.strip()
            print(word)
            time.sleep(delay)
            
elif mode == "2":
    # Mode 2: Search word list for a specific string
    string = input("Enter string to search for:\n")
    file_path = input("Enter word list file path:\n")
    
    with open(file_path) as file:
        words = [line.strip() for line in file]
    
    if string in words:
        print(f"{string} was found in the word list!")
    else:
        print(f"{string} was not found in the word list.")
        
else:
    print("Invalid mode selected. Please select mode 1 or mode 2.")
