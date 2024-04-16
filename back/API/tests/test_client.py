"""Test user"""
import unittest

from main import app

from mock import patch
from mockfirestore import MockFirestore
from modules.client import ClientModule
from models.client import Client
from modules.utils import decrypt, encripty

class TestClient(unittest.TestCase):
    """Test client"""

    def setUp(self):
        self.mock_db = MockFirestore()
        self.patcher = patch(
            'modules.main.MainModule.get_firestore_db', return_value=self.mock_db)
        self.patcher.start()
        self.app = app.test_client()

    def tearDown(self):
        self.patcher.stop()
        self.mock_db.reset()

    def test_post_client(self):
        """ test post client """
        response = self.app.post(path='/clients', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.get_json()['message'], "Bad request not params for client create")

        client_params = {
            'cpf': '318.500.111-33',
            'name': 'Breno Bastos da Silva',
            'email': 'breno17contato@hotmail.com',
            'password': '12345',
            'group': 'cliente',
            'birth_date': '10/07/2001',
            'gender': 'M',
            'billing_address': {
                    'cep': '12345-678',
                    'logradouro': 'Rua Acuti',
                    'numero': '123',
                    'complemento': 'AP 101',
                    'bairro': 'Centro',
                    'cidade': 'São Paulo',
                    'uf': 'SP'
                },
            'delivery_address': [
                {
                    'cep': '54321-876',
                    'logradouro': 'Avenida Belmira Marin',
                    'numero': '456',
                    'complemento': 'AP 202',
                    'bairro': 'Bairro Novo',
                    'cidade': 'São Paulo',
                    'uf': 'SP'
                }
            ]
        }

        response = self.app.post(path='/clients', json=client_params)

        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        self.assertIsNotNone(response_json)
        self.assertIsNotNone(response_json['id'])
        self.assertEqual(response_json['name'], client_params['name'])
        self.assertEqual(response_json['email'], client_params['email'])
        self.assertEqual(response_json['cpf'], client_params['cpf'])
        self.assertEqual(response_json['birth_date'], client_params['birth_date'])
        self.assertEqual(response_json['gender'], client_params['gender'])
        self.assertEqual(response_json['billing_address'], client_params['billing_address'])
        self.assertEqual(response_json['delivery_address'], client_params['delivery_address'])
        self.assertEqual(response_json['group'], client_params['group'])
        self.assertEqual(response_json['active'], True)
        self.assertEqual(
           decrypt(response_json ['password']), client_params['password'])

        response = self.app.post(path='/clients', json=client_params)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.get_json()['message'], "E-mail already registered")
            
        response = self.app.get(path='/client')



    def test_client_sign_in(self):
        """ Test client sign in """
        client_params = {
            'cpf': '318.500.111-33',
            'name': 'Breno Bastos da Silva',
            'email': 'breno17contato@hotmail.com',
            'password': '12345',
            'group': 'cliente',
            'birth_date': '10/07/2001',
            'gender': 'M',
            'billing_address': {
                    'cep': '12345-678',
                    'logradouro': 'Rua Acuti',
                    'numero': '123',
                    'complemento': 'AP 101',
                    'bairro': 'Centro',
                    'cidade': 'São Paulo',
                    'uf': 'SP'
                },
            'delivery_address': [
                {
                    'cep': '54321-876',
                    'logradouro': 'Avenida Belmira Marin',
                    'numero': '456',
                    'complemento': 'AP 202',
                    'bairro': 'Bairro Novo',
                    'cidade': 'São Paulo',
                    'uf': 'SP'
                }
            ]
        }

        response = self.app.post('/client-sign-in', json=client_params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {})

        self.app.post(path='/clients', json=client_params)
        response = self.app.post('/client-sign-in', json=client_params)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.get_json()['id'])

    def test_update_and_get_client(self):
        """ Test update Client """
        client_params = {
            'cpf': '318.500.111-33',
            'name': 'Breno Bastos da Silva',
            'email': 'breno17contato@hotmail.com',
            'password': '12345',
            'group': 'cliente',
            'birth_date': '10/07/2001',
            'gender': 'M',
            'billing_address': {
                    'cep': '12345-678',
                    'logradouro': 'Rua Acuti',
                    'numero': '123',
                    'complemento': 'AP 101',
                    'bairro': 'Centro',
                    'cidade': 'São Paulo',
                    'uf': 'SP'
                },
            'delivery_address': [
                {
                    'cep': '54321-876',
                    'logradouro': 'Avenida Belmira Marin',
                    'numero': '456',
                    'complemento': 'AP 202',
                    'bairro': 'Bairro Novo',
                    'cidade': 'São Paulo',
                    'uf': 'SP'
                }
            ]
        }

        client = ClientModule.create(client_params)
        client_param_update = {
            'cpf': '318.500.000-44',
            'name': 'Breno Teste',
            'email': 'breno18contato@hotmail.com',
            'password': 'batata15',
            'group': 'estoquista',
            'active': False,
            'birth_date': '11/09/2001',
            'gender': 'F',
            'billing_address': {
                    'cep': '12345-123',
                    'logradouro': 'Rua Acuti2',
                    'numero': '1234',
                    'complemento': 'AP 102',
                    'bairro': 'Leste',
                    'cidade': 'São Paulo2',
                    'uf': 'RJ'
                },
            'delivery_address': [
                {
                    'cep': '54321-876',
                    'logradouro': 'Avenida Belmira Acuti2',
                    'numero': '2456',
                    'complemento': 'AP 2044',
                    'bairro': 'Bairro Leste',
                    'cidade': 'São Paulo2',
                    'uf': 'RJ'
                }
            ]
        }

        response = self.app.post('/client/{}'.format(client.id), json=client_param_update)

        response_json = response.get_json()
        self.assertEqual(response_json['name'], client_param_update['name'])
        self.assertEqual(response_json['cpf'], client_param_update['cpf'])
        self.assertEqual(
            decrypt(response_json ['password']), client_param_update['password'])
        self.assertEqual(response_json['group'], client_param_update['group'])
        self.assertEqual(response_json['email'], client_params['email'])
        self.assertEqual(response_json['active'], client_param_update['active'])
        self.assertEqual(response_json['birth_date'], client_param_update['birth_date'])
        self.assertEqual(response_json['gender'], client_param_update['gender'])
        self.assertEqual(response_json['billing_address'], client_param_update['billing_address'])
        self.assertEqual(response_json['delivery_address'], client_param_update['delivery_address'])
        

        response = self.app.get('/client/{}'.format(client.id))

        response_json = response.get_json()
        self.assertEqual(response_json['name'], client_param_update['name'])
        self.assertEqual(response_json['cpf'], client_param_update['cpf'])
        self.assertEqual(
            decrypt(response_json ['password']), client_param_update['password'])
        self.assertEqual(response_json['group'], client_param_update['group'])
        self.assertEqual(response_json['email'], client_params['email'])
        self.assertEqual(response_json['active'], client_param_update['active'])
        self.assertEqual(response_json['birth_date'], client_param_update['birth_date'])
        self.assertEqual(response_json['gender'], client_param_update['gender'])
        self.assertEqual(response_json['billing_address'], client_param_update['billing_address'])
        self.assertEqual(response_json['delivery_address'], client_param_update['delivery_address'])