import requests

request = 'http://127.0.0.1:6000/prime_number/10'

response = requests.get(request).json()

print(response)
