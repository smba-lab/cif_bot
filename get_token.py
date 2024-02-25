# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:37:12 2024

@author: Общий ноут
"""

import requests
import json

# Open the text file and load its content as JSON
with open('get_token_info.txt', 'r') as file:
    token_info = json.load(file)

# get token
def getus():
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    payload='scope=GIGACHAT_API_PERS'
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Accept': 'application/json',
      'RqUID': token_info['RqUID'],
      'Authorization': f"Basic {token_info['Authorization']}"
    }
    
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    
    
    with open('gig.txt', 'w') as file:
        file.write(response.json()['access_token'])

getus()