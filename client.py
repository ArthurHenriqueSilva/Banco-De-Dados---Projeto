import unittest
import requests


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:5000/usuarios"

    def test_get_usuarios(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_criar_usuario(self):
        data = {"cpf": "12345678901", "nome": "Usuario 1", "data_nascimento": "1990-01-01"}
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 201)

    def test_criar_usuario_com_cpf_ja_existente(self):
        data = {"cpf": "12345678901", "nome": "Usuario 2", "data_nascimento": "1995-05-05"}
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 409)

    def test_buscar_usuario(self):
        response = requests.get(f"{self.url}/12345678901")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'cpf': '12345678901', 'nome': 'Usuario 1', 'data_nascimento': '1990-01-01'})

    def test_buscar_usuario_inexistente(self):
        response = requests.get(f"{self.url}/11111111111")
        self.assertEqual(response.status_code, 404)

    def test_remover_usuario(self):
        response = requests.delete(f"{self.url}/12345678901")
        self.assertEqual(response.status_code, 204)

    def test_remover_usuario_inexistente(self):
        response = requests.delete(f"{self.url}/11111111111")
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
