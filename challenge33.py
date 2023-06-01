#!/usr/bin/env python3

# Script: Ops 401 Class 33 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 6/1/23
# Purpose: Add to your malware detection script features to:
# Successfully connect to the VirusTotal API
# Automatically compare your target file’s md5 hash with the hash values of entries on VirusTotal API
# Print to the screen the number of positives detected and total files scanned
# Resources: in class demo, class github, chatgpt.
# did not insert personal API key for security reasons. 



import os
import hashlib
import platform
import time
import requests

API_KEY = ""

def search_files(directory):
    files_searched = 0
    positives_detected = 0
    
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
                print("MD5 Hash: {}".format(md5_hash))
                
                if API_KEY:
                    positives = check_virustotal(md5_hash)
                    print("Positives Detected: {}\n".format(positives))
                    if positives > 0:
                        positives_detected += 1
                else:
                    print("VirusTotal API key not provided. Skipping scan.\n")
    
    print("\nSearch complete.")
    print("Files searched: {}".format(files_searched))
    print("Positives Detected: {}".format(positives_detected))

def calculate_md5(file_path):
    with open(file_path, 'rb') as file:
        hash_md5 = hashlib.md5()
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def check_virustotal(md5_hash):
    url = "https://www.virustotal.com/api/v3/files/{}".format(md5_hash)
    headers = {
        "x-apikey": API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        json_response = response.json()
        if 'data' in json_response and 'attributes' in json_response['data']:
            return json_response['data']['attributes']['last_analysis_stats']['malicious']
    return 0

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
