#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 15:03:04 2021

@author: lizaveta.kuryla
"""

# run mlflow model on 1244 port 
# using comand: mlflow models serve --model-uri runs:/1f6bfe875e874cdb83576466ba53c712/model --port 1244

import json
import requests

url = 'http://127.0.0.1:1244/invocations'
headers = {'Content-Type': 'application/json'}

request_data = json.dumps({"columns":["age", "salary"],"data":[[42, 50000]]})
response = requests.post(url,request_data,headers=headers)
print (response.text)
