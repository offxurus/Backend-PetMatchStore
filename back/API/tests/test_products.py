"""Test products"""
import unittest

from modules.products import ProductsModule
from main import app

from mock import patch
from mockfirestore import MockFirestore

from models.products import Products
from modules.utils import encripty

class TestProducts(unittest.TestCase):
    """Test products"""

    def setUp(self):
        self.mock_db = MockFirestore()
        self.patcher = patch(
            'modules.main.MainModule.get_firestore_db', return_value=self.mock_db)
        self.patcher.start()
        self.app = app.test_client()
    
    def tearDown(self):
        self.patcher.stop()
        self.mock_db.reset()

    def test_post_products(self):
        """ test create products """
        products_params = {"name": "Bola","price": 120.35, "quantity": 1}

        response = self.app.post(
            path='/products', json=products_params)
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        self.assertIsNotNone(response_json['id'])
        self.assertEqual(response_json['name'], products_params['name'])
        self.assertEqual(response_json['code'], 1)
        self.assertEqual(response_json['price'], products_params['price'])
        self.assertEqual(response_json['quantity'], products_params['quantity'])
        self.assertEqual(response_json['active'], True)


        response = self.app.post(
            path='/products', json=products_params)
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        
        self.assertEqual(response_json['code'], 2)

    def test_get_products(self):
        """ test get products """
        products_params = {
            "name": "Bola","price": 120.35, "quantity": 1
        }
        for _ in range(0, 20):
            ProductsModule.create(products_params)

        response = self.app.get(path='/products?offset=0')
        self.assertEqual(len(response.get_json()['products']), 10)
        response_json = response.get_json()
        response = self.app.get(path='/products?offset={0}'.format(response_json['cursor']))
        self.assertEqual(len(response.get_json()['products']), 10)
        self.assertEqual(response_json['products'][0]['images'], [])



    def test_update_and_get_product(self):
        """Test update Product"""
        product_param_create = {
            "name": "Bola","price": 120.35, "quantity": 1
        }
        product = ProductsModule.create(product_param_create)
        product_param_update = {
            "name": "Carro","price": 200.35, "quantity": 2, "active":False
        }

        response = self.app.post('/product/{}'.format(product.id), json=product_param_update)

        response_json = response.get_json()
        self.assertEqual(response_json['name'], product_param_update['name'])
        self.assertEqual(response_json['price'], product_param_update['price'])
        self.assertEqual(response_json['quantity'], product_param_update['quantity'])
        self.assertEqual(response_json['active'], product_param_update['active'])


        response = self.app.get('/product/{}'.format(product.id))

        response_json = response.get_json()
        self.assertEqual(response_json['name'], product_param_update['name'])
        self.assertEqual(response_json['price'], product_param_update['price'])
        self.assertEqual(response_json['quantity'], product_param_update['quantity'])
        self.assertEqual(response_json['active'], False)





    
        