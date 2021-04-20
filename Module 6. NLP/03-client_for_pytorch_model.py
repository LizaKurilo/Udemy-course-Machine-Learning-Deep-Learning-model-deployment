#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:24:32 2021

@author: lizaveta.kuryla
"""

import json
import requests

url = 'http://0370826f1e01.ngrok.io/predict'

request_data = json.dumps({'sentence':'Bad perfomance by India'})
response = requests.post(url, request_data)

print(response.text)