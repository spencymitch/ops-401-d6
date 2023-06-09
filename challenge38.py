#!/usr/bin/env python3

# Script: Ops 401 Class 38 Ops Challenge
# Author: Spencer Mitchell
# Date of latest revision: 6/8/23
# Purpose:Fully annotate any missing comments and populate any missing variables/code
# Resources: class demo/github, chatgpt




import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

def get_all_forms(url):
    """
    Retrieves all HTML forms from a given URL.

    Args:
        url (str): The URL to scrape forms from.

    Returns:
        list: A list of BeautifulSoup objects representing the HTML forms.
    """
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """
    Extracts details from a given HTML form.

    Args:
        form (BeautifulSoup): The BeautifulSoup object representing the HTML form.

    Returns:
        dict: A dictionary containing the form details, including the action URL, method, and input fields.
    """
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, value):
    """
    Submits a form with provided data to a target URL.

    Args:
        form_details (dict): A dictionary containing the form details.
        url (str): The base URL of the target website.
        value (str): The value to be filled in the form fields.

    Returns:
        requests.Response: The response object returned after submitting the form.
    """
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def scan_xss(url):
    """
    Scans a given URL for XSS vulnerabilities in forms.

    Args:
        url (str): The URL to scan for XSS vulnerabilities.

    Returns:
        bool: True if XSS vulnerability is detected, False otherwise.
    """
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = '<script>alert("XSS Vulnerability");</script>'  # Injected JavaScript code to test XSS vulnerability
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))
