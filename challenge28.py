#!/usr/bin/env python3

# Script: Ops 401 Class 28 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 5/24/23
# Purpose: Use StreamHandler and FileHandler in your Python script.
# Resources: in class demo, class github, and chatgpt.

import time
import ping3
import smtplib
import logging
from logging.handlers import RotatingFileHandler
from email.message import EmailMessage
from getpass import getpass

# Set up logging with both StreamHandler and FileHandler
log_file = 'uptime_sensor.log'
max_file_size = 1024 * 1024  # 1MB
backup_count = 5  # Number of backup log files

# Set up the StreamHandler to output logs to the terminal
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))

# Set up the FileHandler to write logs to a local file
file_handler = RotatingFileHandler(log_file, maxBytes=max_file_size, backupCount=backup_count)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))

# Create a logger and add the handlers
logger = logging.getLogger()
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

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

    # log status
    logger.info(f"{status} to {ip}")

    time.sleep(interval)
