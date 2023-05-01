#!/usr/bin/env python3

# Script: Ops 401 Class 11 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 5/1/23
# Purpose: Utilize the scapy library
# Define host IP
# Define port range or specific set of ports to scan
# Test each port in the specified range using a for loop
# If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
# If flag 0x14 received, notify user the port is closed.
# If no flag is received, notify the user the port is filtered and silently dropped.
# Resources: In class demo, the class github, and chatgpt helped with elif statements and commenting out each line. 



from scapy.all import *

# Define the target host IP address
target_ip = "192.168.0.1"

# Define the port range to scan
port_range = range(1, 101)  # Scans ports 1-100

# Loop through each port in the range
for port in port_range:
    # Create the SYN packet
    syn_packet = IP(dst=target_ip) / TCP(dport=port, flags="S")

    # Send the SYN packet and receive the response
    syn_response = sr1(syn_packet, timeout=1, verbose=0)

    # Check the response flags to determine the state of the port
    if syn_response is None:
        print(f"Port {port} filtered (silently dropped).")
    elif syn_response.haslayer(TCP) and syn_response.getlayer(TCP).flags == 0x12:
        # Create the RST packet to close the connection
        rst_packet = IP(dst=target_ip) / TCP(dport=port, flags="R")

        # Send the RST packet
        send(rst_packet, verbose=0)

        print(f"Port {port} open.")
    elif syn_response.haslayer(TCP) and syn_response.getlayer(TCP).flags == 0x14:
        print(f"Port {port} closed.")
    else:
        print(f"Port {port} filtered (silently dropped).")
