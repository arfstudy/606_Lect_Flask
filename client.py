import requests

# response = requests.get('http://127.0.0.1:5000/hello/world')

# response = requests.post('http://127.0.0.1:5000/hello/world/1',
#                          json={"name": 'user_2', 'password': '123gwesgtewt544'},
#                          headers={"token": "secret_token"},
#                          params={"k1": "v1", "k2": "v2"})

# response = requests.patch('http://127.0.0.1:5000/user', json={"name": 'user_1', 'password': '123gwesgtewt544'})

# response = requests.delete('http://127.0.0.1:5000/hello/user/7')

# response = requests.get('http://127.0.0.1:5000/user/7')

print(response.status_code)
print(response.headers["Content-Type"])
print(response.text)