#!/usr/bin/env python3

# Script: Ops 401 Class 06 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 4/24/23
# Purpose: Add a feature capability to your Python encryption tool to:
# Alter the desktop wallpaper on a Windows PC with a ransomware message
# Create a popup window on a Windows PC with a ransomware message
# Make this feature optional. In the user menu prompt, add this as a ransomware simulation option.
# Resources: The class repo demo, in class demo, and chatgpt helped me add the remaining malware options. I was unable to run this as
# I cannot create an environment that allows it to run. 



import os
import base64
from cryptography.fernet import Fernet
import ctypes

# Generate a key for encryption and decryption
def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

# Load the encryption key from file
def load_key():
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key

# Encrypt a file
def encrypt_file(file_path):
    key = load_key()
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Decrypt a file
def decrypt_file(file_path):
    key = load_key()
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

# Encrypt a message
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encoded_message = message.encode()
    encrypted_message = f.encrypt(encoded_message)
    return base64.urlsafe_b64encode(encrypted_message).decode()

# Decrypt a message
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decoded_message = base64.urlsafe_b64decode(encrypted_message)
    decrypted_message = f.decrypt(decoded_message)
    return decrypted_message.decode()

# Change the desktop wallpaper
def change_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)

# Create a popup message
def popup_message(title, message):
    ctypes.windll.user32.MessageBoxW(None, message, title, 0)

# User menu prompt
while True:
    mode = input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Simulate ransomware (optional)\n6. Exit\n")
    if mode == "1":
        # Encrypt a file
        file_path = input("Enter the file path: ")
        encrypt_file(file_path)
    elif mode == "2":
        # Decrypt a file
        file_path = input("Enter the file path: ")
        decrypt_file(file_path)
    elif mode == "3":
        # Encrypt a message
        message = input("Enter the message to encrypt: ")
        encrypted_message = encrypt_message(message)
        print("Encrypted message:", encrypted_message)
    elif mode == "4":
        # Decrypt a message
        encrypted_message = input("Enter the message to decrypt: ")
        decrypted_message = decrypt_message(encrypted_message)
        print("Decrypted message:", decrypted_message)
    elif mode == "5":
        # Simulate ransomware
        change_wallpaper('path/to/image.jpg')
        popup_message('Ransomware message', 'Your files have been encrypted. Pay the ransom to get them back.')
    elif mode == "6":
        # Exit
        break
    else:
        print("Invalid mode. Please select a valid mode.")
