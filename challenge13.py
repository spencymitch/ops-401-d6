#!/usr/bin/env python3

# Script: Ops 401 Class 12 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 5/1/23
# Purpose: Refactor our previous code.
# Resources: In class demo, class repo, and chatgpt. 

import socket
import struct
from scapy.all import *

def port_scan(host):
    ports = range(1, 1001) # Change this range to fit your needs
    open_ports = []
    closed_ports = []
    filtered_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
                send(IP(dst=host)/TCP(dport=port, flags="R"), verbose=0) # Send RST packet to gracefully close connection
            else:
                closed_ports.append(port)
            sock.close()
        except:
            filtered_ports.append(port)
    print("Open ports: ", open_ports)
    print("Closed ports: ", closed_ports)
    print("Filtered ports: ", filtered_ports)

def network_scanner():
    ip_address = input("Enter an IP address to target: ")
    cidr = input("Enter a CIDR block: ")
    net = ipaddress.ip_network(ip_address+"/"+cidr, strict=False)
    online_hosts = []
    offline_hosts = []
    for host in net.hosts():
        if host == net.network_address or host == net.broadcast_address:
            continue
        icmp = IP(dst=str(host))/ICMP()
        resp = sr1(icmp, timeout=2, verbose=0)
        if resp == None:
            offline_hosts.append(host)
            print(str(host) + " is down or unresponsive.")
        elif resp.type == 3 and resp.code in [1, 2, 3, 9, 10, 13]:
            offline_hosts.append(host)
            print(str(host) + " is actively blocking ICMP traffic.")
        else:
            online_hosts.append(host)
            print(str(host) + " is responding.")
            port_scan(str(host))
    print("Online hosts: ", online_hosts)
    print("Offline hosts: ", offline_hosts)
    print("Number of online hosts: ", len(online_hosts))

network_scanner()
