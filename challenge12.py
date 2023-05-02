#!/usr/bin/env python3

# Script: Ops 401 Class 12 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 5/2/23
# Purpose:Add the following features to your Network Security Tool:

# User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set
# ICMP Ping Sweep tool
# Prompt user for network address including CIDR block, for example “10.10.0.0/24”
# Careful not to populate the host bits!
# Create a list of all addresses in the given network
# Ping all addresses on the given network except for network address and broadcast address
# If no response, inform the user that the host is down or unresponsive.
# If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
# Otherwise, inform the user that the host is responding.
# Count how many hosts are online and inform the user.
# Resource: In class demo, class remo, and chatgpt








from scapy.all import *

def tcp_port_range_scanner():
    # Define the target host IP address
    target_ip = input("Enter target IP address: ")

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

def icmp_ping_sweep():
    # Prompt the user for the network address with CIDR block
    network_addr = input("Enter network address with CIDR block (e.g. 10.10.0.0/24): ")

    # Parse the network address and CIDR block
    network, cidr_block = network_addr.split('/')
    cidr_block = int(cidr_block)

    # Calculate the number of host bits
    num_host_bits = 32 - cidr_block

    # Calculate the number of hosts in the network
    num_hosts = 2 ** num_host_bits - 2

    # Create a list of all addresses in the network
    network_address = IPv4Address(network)
    addresses = [str(network_address + i) for i in range(1, num_hosts+1)]

    # Loop through each address in the network
    online_hosts = 0
    for address in addresses:
        # Create the ICMP ping request packet
        ping_request = IP(dst=address) / ICMP()

        # Send the ICMP ping request and receive the response
        ping_response = sr1(ping_request, timeout=1, verbose=0)

        # Check the ICMP response type and code to determine the state of the host
        if ping_response is None:
            print(f"Host {address} is down or unresponsive.")
        elif ping_response.type == 3 and ping_response.code in [1, 2, 3, 9, 10, 13]:
            print(f"Host {address} is actively blocking ICMP traffic.")
        else:
            print(f"Host {address} is online and responding.")
            online_hosts += 1

    # Print the number of online hosts
    print(f"Number of online hosts: {online_hosts}")


# Prompt the user for the tool mode
while True:
    tool_mode = input("Enter tool mode (1 for TCP Port Range Scanner, 2 for ICMP Ping Sweep): ")
    if tool_mode == "1":
        tcp_port_range_scanner()
        break
    elif tool_mode == "2":
       
