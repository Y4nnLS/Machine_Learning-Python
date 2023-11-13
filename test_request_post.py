import requests

url = 'http://127.0.0.1:5000/happy'

with open('exemplo.json', 'r') as json_file:
    headers = { 'Content-Type': 'application/json' }
    json_body = json_file.read()
    response = requests.post(url, data=json_body, headers=headers, timeout=3)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Erro ', response.status_code)

