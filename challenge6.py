#!/usr/bin/env python3

# Script: Ops 401 Class 06 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 4/24/23
# Purpose: In Python, create a script that utilizes the cryptography library to: encrypt and decrypt files and messages. 
# Resources: The demo in the class repo, and chatgpt helped me get rid of my many functions and loops and consolidated into a menu.
# Also my ubuntu server somehow died and I could not save this in my linux environment. I was unable to run it. 

import os
from cryptography.fernet import Fernet

# Generate a random key to encrypt and decrypt data
key = Fernet.generate_key()
fernet = Fernet(key)

# Prompt the user to select a mode
mode = input("Select a mode (1=encrypt file, 2=decrypt file, 3=encrypt message, 4=decrypt message): ")

# Encrypt or decrypt a file
if mode == '1':
    filepath = input("Enter the filepath of the target file: ")
    with open(filepath, 'rb') as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(filepath, 'wb') as f:
        f.write(encrypted)
    print("File encrypted successfully.")
elif mode == '2':
    filepath = input("Enter the filepath of the target file: ")
    with open(filepath, 'rb') as f:
        data = f.read()
    decrypted = fernet.decrypt(data)
    with open(filepath, 'wb') as f:
        f.write(decrypted)
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

# Handle invalid mode selection
else:
    print("Invalid mode selected.")
