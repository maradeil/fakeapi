import requests
import json

url = "https://my-json-server.typicode.com/maradeil/fakeapi/posts"

payload = json.dumps({
    'title': 'foo',
    'body': 'bar',
    'userId': 2,
  })
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
