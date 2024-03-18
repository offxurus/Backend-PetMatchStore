import uuid

from modules.main import MainModule

class Products(object):

    _collection_name = 'Products'


    def __init__(self, **args):
        self.id = args.get('id',uuid.uuid4().hex)
        self.code = args.get("code")
        self.name = args.get('name')
        self.price = args.get('price')
        self.quantity = args.get('quantity')
        self.active = args.get('active')


    def save(self):
        """Save Products"""
        MainModule.get_firestore_db().collection(
            self._collection_name).document(self.id).set(self.to_dict())
        
    def to_dict(self):
        """Transform products in dict format"""
        return {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'active': self.active
        }
    
    @classmethod
    def get_next_cod(cls):
        products = cls.get_products()
        products_list = []
        for product in products:
            products_list.append(product.to_dict())
        last_cod = sorted(products_list, key=lambda x: x['code'])
        if last_cod:
            return last_cod[0]['code'] + 1
        else:
            return 1
    
    @classmethod
    def get_products(cls):
        """
        Get products
        """
        return MainModule.get_firestore_db().collection(
            cls._collection_name).limit(10).stream()
    
    @classmethod
    def get_product(cls, product_id):
        """
        Get product
        """
        product = MainModule.get_firestore_db().collection(
            cls._collection_name).document(product_id).get()
        if product.exists:
            return Products(**product.to_dict())
        return None