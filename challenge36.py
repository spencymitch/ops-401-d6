#!/usr/bin/env python3

# Script: Ops 401 Class 36 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 6/6/23
# Purpose: Challenge36 assignment parameters. 
# Resources: in class demo, class github, and chatgpt


import subprocess
import os
import sys
import socket
import time
import telnetlib

def banner_grabbing(target, port):
    print(f"Banner grabbing for {target}:{port}")
    print("Using netcat:")
    nc_process = subprocess.Popen(["nc", "-vz", target, port], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    nc_output, nc_error = nc_process.communicate()
    print(nc_output.decode())
    print("Using telnet:")
    try:
        telnet_socket = telnetlib.Telnet(target, port)
        telnet_output = telnet_socket.read_all().decode()
        print(telnet_output)
        telnet_socket.close()
    except ConnectionRefusedError:
        print("Connection refused.")

def nmap_scan(target):
    print(f"Performing Nmap scan for {target}")
    nmap_process = subprocess.Popen(["nmap", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    nmap_output, nmap_error = nmap_process.communicate()
    print(nmap_output.decode())

def main():
    target = input("Enter a URL or IP address: ")
    port = input("Enter a port number: ")

    banner_grabbing(target, port)
    nmap_scan(target)

if __name__ == "__main__":
    main()
