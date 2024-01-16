import requests
import json

url = "https://my-json-server.typicode.com/maradeil/fakeapi/posts"

payload = json.dumps({
    'nome': 'serginho bom de prato',
    'função': 'comer grao de bico',
    'userId': 3,
  })
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
