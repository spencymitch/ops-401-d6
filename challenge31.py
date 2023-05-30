#!/usr/bin/env python3

# Script: Ops 401 Class 31 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 5/30/23
# Purpose: Prompt the user to type in a file name to search for.
# Prompt the user for a directory to search in.
# Search each file in the directory by name.
# For each positive detection, print to the screen the file name and location.
# At the end of the search process, print to the screen how many files were searched and how many hits were found.
# The script must successfully execute on both Ubuntu Linux 20.04 Focal Fossa and Windows 10.
# Resources: in class demo with JB, class github, and chatgpt.

import os
import platform

def search_files(file_name, search_directory):
    files_searched = 0
    hits_found = 0
    
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            if file == file_name:
                hits_found += 1
                file_path = os.path.join(root, file)
                print("Hit found: {} (Location: {})".format(file, file_path))
                
            files_searched += 1
    
    print("\nSearch complete.")
    print("Files searched: {}".format(files_searched))
    print("Hits found: {}".format(hits_found))

def get_user_input(prompt):
    if platform.system() == "Windows":
        return input(prompt)
    else:
        return input(prompt).decode('utf-8')

def main():
    file_name = get_user_input("Enter the file name to search for: ")
    search_directory = get_user_input("Enter the directory to search in: ")

    search_files(file_name, search_directory)

if __name__ == "__main__":
    main()
