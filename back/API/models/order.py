import uuid

from modules.main import MainModule

class Order(object):

    _collection_name = 'order'


    def __init__(self, **args):
        self.id = args.get('id',uuid.uuid4().hex)
        self.products_order = args.get('products_order', [])
        self.total_price = args.get('total_price')


    def save(self):
        """Save Orders"""
        MainModule.get_firestore_db().collection(
            self._collection_name).document(self.id).set(self.to_dict())
        
    def to_dict(self):
        """Transform orders in dict format"""
        return {
            'products_order': self.products_order,
            'total_price': self.total_price
        }
    
    
    @classmethod
    def get_order(cls):
        """
        Get order
        """
        order = MainModule.get_firestore_db().collection(
            cls._collection_name).document().get()
        if order.exists:
            return Order(**order.to_dict())
        return None
