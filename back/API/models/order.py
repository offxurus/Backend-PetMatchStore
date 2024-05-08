import uuid

from modules.main import MainModule
from datetime import datetime

class Order(object):

    _collection_name = 'Order'


    def __init__(self, **args):
        self.id = args.get('id')
        self.products_order = args.get('products_order', [])
        self.total = args.get('total')
        self.currentUser = args.get('currentUser')
        self.installments = args.get('installments')
        self.defaultAddress = args.get('defaultAddress')
        self.statusOrder = args.get('statusOrder')
        self.freteValue = args.get('freteSelecionado')
        self.dateOrder = args.get('dateOrder')


    def save(self):
        """Save Orders"""
        MainModule.get_firestore_db().collection(
            self._collection_name).document(self.id).set(self.to_dict())
        
    def to_dict(self):
        """Transform orders in dict format"""
        return {
            'id': self.id,
            'products_order': self.products_order,
            'total': self.total,
            'currentUser':self.currentUser,
            'installments': self.installments,
            'defaultAddress': self.defaultAddress,
            'statusOrder': self.statusOrder,
            'freteSelecionado': self.freteValue,
            'dateOrder': self.dateOrder.strftime('%Y-%m-%d') if self.dateOrder else None
        }
    
    
    
    @classmethod
    def get_order(cls, order_id = None):
        """
        Get order
        """
        if order_id:
            order = MainModule.get_firestore_db().collection(
                cls._collection_name).document(order_id).get()
            if order.exists:
                return Order(**order.to_dict())
        else:
            return MainModule.get_firestore_db().collection(
                cls._collection_name).stream()
        return None
