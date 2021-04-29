#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:24:32 2021

@author: lizaveta.kuryla
"""

import json
import requests

url = 'https://us-central1-coastal-mender-307721.cloudfunctions.net/nlp-tf-demo'

request_data = json.dumps({'sentence':'good perfomance by India'})
response = requests.post(url, request_data)

print(response.text)