#!/usr/bin/env python3

# Copyright (C) Ben McGinnes, 2013
# ben@adversary.org
#

import requests
import sys

l = len(sys.argv)

if l == 1:
    target = input("Enter the URL to shorten via is.gd: ")
    seturl = input("Specify variable in shortened URL (5-30 alphanumeric characters): ")
elif l == 2:
    target = sys.argv[1]
    seturl = input("Specify variable in shortened URL (5-30 alphanumeric characters): ")
elif l == 3:
    target = sys.argv[1]
    seturl = sys.argv[2]
else:
    target = input("Enter the URL to shorten via is.gd: ")
    seturl = input("Specify variable in shortened URL (5-30 alphanumeric characters): ")

url = "http://is.gd/create.php"
payload = {"format": "json", "url": target, "logstats": "1", "shorturl": seturl}

r = requests.get(url, params=payload)

print("""
The URL of the API Access:

    %s

The URL to be shortened:

    %s

The URL of the shortened link:

    %s
""" % (r.url, target, r.json()["shorturl"]))
