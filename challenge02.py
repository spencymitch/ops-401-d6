#!/usr/bin/env python3

# Script: Ops 401 Class 02 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 4/18/23
# Purpose: In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.
# Resources: Marco Vasquez's demo and chatgpt helped me define the loop.

import time
import ping3

# functions defined 
ip = "192.168.1.1" # IP address to test
interval = 2 # time interval in seconds between pings

while True:
    try:
        response_time = ping3.ping(ip)
        if response_time is not None:
            status = "Network Active"
        else:
            status = "Network Error"
    except:
        status = "Network Error"
    
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")
    print(f"{timestamp} {status} to {ip}")
    
    time.sleep(interval)