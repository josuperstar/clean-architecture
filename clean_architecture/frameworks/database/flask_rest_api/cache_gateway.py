import requests
api_url = 'http://127.0.0.1:8000/1'
response = requests.get(api_url)
print(response)
print(response.text)
