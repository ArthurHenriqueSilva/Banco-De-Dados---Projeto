import unittest
import requests
url = "http://127.0.0.1:5000/usuarios"
data = {"cpf": "12345678901", "nome": "Usuario 1", "data_nascimento": "1990-01-01"}

# teste de inserção 
response = requests.post(url, json=data)
assert response.status_code == 200
print(response.json)

# teste de  
response = requests.get(url)
assert response.status_code == 200
print(response.json)

# teste de busca de usuário por cpf
response = requests.get(f"{url}/12345678901")
assert response.status_code == 200
print(response.json)
