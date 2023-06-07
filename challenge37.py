#!/usr/bin/env python3

# Script: Ops 401 Class 37 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 6/7/23
# Purpose: 
# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
# - Generate a .html file to capture the contents of the HTTP response
# - Open it with Firefox
# Resources: in class demo, class github, and chatgpt

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import webbrowser

targetsite = "http://www.whatarecookies.com/cookietest.asp"

response = requests.get(targetsite)
cookie = response.cookies

# Send the cookie back to the site
response = requests.get(targetsite, cookies=cookie)

# Capture the contents of the HTTP response
html_content = response.text

# Generate a timestamp for the filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Create an HTML file with the contents of the response
filename = f"response_{timestamp}.html"
with open(filename, "w") as file:
    file.write(html_content)

# Open the HTML file with Firefox
firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Replace with the path to your Firefox executable
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
webbrowser.get('firefox').open(filename)

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)
