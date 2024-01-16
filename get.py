import requests

url = "https://my-json-server.typicode.com/maradeil/fakeapi/funcoes"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)