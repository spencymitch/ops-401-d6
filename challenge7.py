#!/usr/bin/env python3

# Script: Ops 401 Class 07 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 4/25/23
# Purpose: In Python, create a script that utilizes the cryptography library to: encrypt and decrypt files and messages. 
# Resources: The demo in the class repo, Alexs in class demo. and chatgpt helped me get rid of my many functions and loops and consolidated into a menu. It also helped me with os.walkpath 
# Also my ubuntu server somehow died and I could not save this in my linux environment. I was unable to run it. 



import os
from cryptography.fernet import Fernet

# Generate a random key to encrypt and decrypt data
key = Fernet.generate_key()
fernet = Fernet(key)

def encrypt_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(filepath, 'wb') as f:
        f.write(encrypted)

def decrypt_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    decrypted = fernet.decrypt(data)
    with open(filepath, 'wb') as f:
        f.write(decrypted)

def encrypt_folder(folderpath):
    for root, dirs, files in os.walk(folderpath):
        for file in files:
            filepath = os.path.join(root, file)
            encrypt_file(filepath)
    print("Folder encrypted successfully.")

def decrypt_folder(folderpath):
    for root, dirs, files in os.walk(folderpath):
        for file in files:
            filepath = os.path.join(root, file)
            decrypt_file(filepath)
    print("Folder decrypted successfully.")

# Prompt the user to select a mode
mode = input("Select a mode (1=encrypt file, 2=decrypt file, 3=encrypt message, 4=decrypt message, 5=encrypt folder, 6=decrypt folder): ")

# Encrypt or decrypt a file
if mode == '1':
    filepath = input("Enter the filepath of the target file: ")
    encrypt_file(filepath)
    print("File encrypted successfully.")
elif mode == '2':
    filepath = input("Enter the filepath of the target file: ")
    decrypt_file(filepath)
    print("File decrypted successfully.")

# Encrypt or decrypt a message
elif mode == '3':
    message = input("Enter the cleartext message to encrypt: ")
    encrypted = fernet.encrypt(message.encode())
    print(encrypted.decode())
elif mode == '4':
    message = input("Enter the ciphertext message to decrypt: ")
    decrypted = fernet.decrypt(message.encode())
    print(decrypted.decode())

# Recursively encrypt or decrypt a folder
elif mode == '5':
    folderpath = input("Enter the folder path to encrypt: ")
    encrypt_folder(folderpath)
elif mode == '6':
    folderpath = input("Enter the folder path to decrypt: ")
    decrypt_folder(folderpath)

# Handle invalid mode selection
else:
    print("Invalid mode selected.")
