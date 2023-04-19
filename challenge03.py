#!/usr/bin/env python3

# Script: Ops 401 Class 02 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 4/19/23
# Purpose: Ask the user for an email address and password to use for sending notifications.
# Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
# Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.
# Resources: Marco's demo and chat gpt helped with sending the email to the correct destination.
# Full disclosure, this script was not tested fully



import time
import ping3
import smtplib
from email.message import EmailMessage
from getpass import getpass

# functions defined
ip = "192.168.1.1" # IP address to test
interval = 2 # time interval in seconds between pings

# prompt user for email credentials
email = input("Enter your email address: ")
password = getpass("Enter your email password: ")

# set up email server
smtp_server = "smtp.gmail.com" # email provider's SMTP server
smtp_port = 587 # email provider's SMTP port
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(email, password)

# initialize previous status to "Network Active"
prev_status = "Network Active"

while True:
    try:
        response_time = ping3.ping(ip)
        if response_time is not None:
            status = "Network Active"
        else:
            status = "Network Error"
    except:
        status = "Network Error"
    
    # send email notification if status changed
    if status != prev_status:
        message = EmailMessage()
        message["From"] = email
        message["To"] = email
        message["Subject"] = f"{ip} status changed"
        body = f"{ip} status changed from {prev_status} to {status} at {time.strftime('%Y-%m-%d %H:%M:%S.%f')}"
        message.set_content(body)
        server.send_message(message)
    
    prev_status = status
    
    # print status to console
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")
    print(f"{timestamp} {status} to {ip}")
    
    time.sleep(interval)