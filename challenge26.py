#!/usr/bin/env python3

# Script: Ops 401 Class 26 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 5/22/23
# Purpose: Add logging capabilities to your Python tool using the logging library.
# Experiment with log types. Build in some error handling, then induce some errors. Send log data to a file in the local directory.
# Confirm your logging feature is working as expected.
# Resources: in class demo, class github, and chatgpt. 



import time
import ping3
import smtplib
import logging
from email.message import EmailMessage
from getpass import getpass

# Set up logging
logging.basicConfig(
    filename='uptime_sensor.log',
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.INFO
)

# functions defined
ip = "192.168.1.1"  # IP address to test
interval = 2  # time interval in seconds between pings

# prompt user for email credentials
email = input("Enter your email address: ")
password = getpass("Enter your email password: ")

# set up email server
smtp_server = "smtp.gmail.com"  # change to your email provider's SMTP server
smtp_port = 587  # change to your email provider's SMTP port
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

    # log status
    logging.info(f"{status} to {ip}")

    time.sleep(interval)
