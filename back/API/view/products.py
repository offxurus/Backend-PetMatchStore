from flask_restful import Resource
from flask import request
from models.products import Products
from modules.products import ProductsModule



class ProductsHandler(Resource):

    def post(self):
        """Create a new product"""
        try:
            if not request.json:
                return {"message": "Bad request not params for products create"}, 400

            products = ProductsModule.create(request.json)

            return products.to_dict()

        except Exception as error:
            return {
                'message': 'Error on create a new product',
                'details': str(error)
            }, 500
        
    def get(self):
        """Get Products"""
        try:
            response = {"products": [], "cursor": 0}
            products, cursor = Products.get_products(int(request.args.get('offset')))
            for product in products:
                products_json = product.to_dict()
                response['products'].append(products_json)
            response['products'] = sorted(response['products'], key=lambda x: x['code'], reverse=True)
            response['cursor'] = cursor       
            return response

        except Exception as error:
            return {
              'message': 'Error on get Products',
              'details': str(error)
            }, 500
        
class ProductHandler(Resource):
    """Product handler"""
    def get(self, product_id):
        """Get Product"""
        try:
            product = Products.get_product(product_id)
            if product:
                return product.to_dict()
            return {}
        except Exception as error:
            return {
            'message': 'Error on get Product',
            'details': str(error)
        }, 500

    def post(self, product_id):
        """Update a product"""
        try:
            product = Products.get_product(product_id)
            request_params = request.json

            if not request.json:
                return {"message": "Bad request not params for update product"}, 400
            
            if not product:
                return {"message": "product not found"}, 400
            
            ProductsModule.update(request_params, product)
            return product.to_dict()
                
        except Exception as error:
            return {
                'message': 'Error on Update a Product',
                'details': str(error)
            }, 500
    