# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

import json
import requests

url = 'http://35.232.150.149:8005/model'

request_data = json.dumps({'age':42, 'salary':50000})
response = requests.post(url, request_data)

print(response.text)