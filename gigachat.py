# -*- coding: utf-8 -*-
"""
Gigachat.py to get description about crystal structure by Gigachat API
and write it into info.txt
"""

import requests
import json
import re
import toolboxer

# get token
with open('gig.txt', 'r') as file:
    TOKENUS = file.read()

cif_info = toolboxer.cif_info()

url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

payload = json.dumps({
  "model": "GigaChat:latest",
  "messages": [
    {
      "role": "user",
      "content": f'Расскажи о {cif_info}'
    }
  ],
  "temperature": 1,
  "top_p": 0.1,
  "n": 1,
  "stream": False,
  "max_tokens": 512*2,
  "repetition_penalty": 1
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': f'Bearer {TOKENUS}'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)


with open('info.txt', 'w', encoding="utf-8") as file:
    file.write(response.json()['choices'][0]['message']['content'])
