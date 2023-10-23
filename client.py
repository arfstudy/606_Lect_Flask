import requests

# response = requests.get('http://127.0.0.1:5000')
# response = requests.post('http://127.0.0.1:5000/hello/world/1')

# response = requests.post('http://127.0.0.1:5000/hello/world/1?k3=v3',
#                          json={"name": 'user_2', 'password': '123gwesgtewt544'},
#                          headers={"token": "my_Secret_token"},
#                          params={"k1": "v1", "k2": "v2"})

print('  Получен ответ:')

response = requests.post('http://127.0.0.1:5000/user', json={"name": 'user_4', 'password': '123gwesgtewt544'})

# response = requests.patch('http://127.0.0.1:5000/user/3', json={"name": 'new_user_name', 'password': '123gwesgtewt544'})

# response = requests.delete('http://127.0.0.1:5000/user/3')

print(response.status_code)
print(response.headers["Content-Type"])
print(response.text)

# response = requests.get('http://127.0.0.1:5000/user/3')
#
# print(response.status_code)
# print(response.headers["Content-Type"])
# print(response.text)
