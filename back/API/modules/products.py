""" Products Module """
from models.products import Products

class ProductsModule(object):
    """Products module"""

    @staticmethod
    def create(params):
        """
        Create new products
        :param params: products dict(JSON)
        return products: Products
        """
        products = Products()
        products.name = params['name']
        products.code = Products.get_next_cod()
        products.price = params['price']
        products.quantity = params['quantity']
        products.active = True
        products.image_default = params['images_default']
        products.description = params['description']
        products.rating = params['rating']

        products.save()
        return products
    
    @staticmethod
    def update(params, product):
        """
        Update product
        :param params: product dict
        return product: Product
        """
         
        if params.get('name'):
            product.name = params['name']
        if params.get('price'):
            product.price = params['price']
        if params.get('quantity'):
            product.quantity = params['quantity']
        if params.get('active') != None:
            product.active = params['active']
        if params.get('image_default'):
            product.image_default = params['image_default']
        if params.get('description'):
            product.description = params['description']
        if params.get('rating'):
            product.rating = params['rating']


        product.save()
        return product