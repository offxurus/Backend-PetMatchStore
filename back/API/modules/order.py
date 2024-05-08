""" Order Module """
from models.order import Order
from datetime import datetime

class OrderModule(object):
    """Order Module"""

    @staticmethod
    def create(params):
        """
        Create new order
        :param params: orders dict(JSON)
        return orders: orders
        """
        order = Order()
        order.id = params['id']
        order.products_order = params['cartItems']
        order.total = params['total']
        order.currentUser = params['currentUser']
        order.installments = params.get('installments')
        order.defaultAddress = params['defaultAddress']
        order.statusOrder = 'Aguardando pagamento'
        order.freteValue = params['freteSelecionado']
        order.dateOrder = datetime.now()
        

        order.save()
        return order
    
    @staticmethod
    def update(params, order):
        """
        Update order
        :param params: order dict
        :param order: Order object to be updated
        return order: updated order
        """       

        if params.get('products_order'):
            order.products_order = params['products_order']
        if params.get('total'):
            order.total = params['total']
        if params.get('currentUser'):
            order.currentUser = params['currentUser']
        if params.get('installments'):
            order.installments = params['installments']
        if params.get('defaultAddress'):
            order.defaultAddress = params['defaultAddress']
        if params.get('freteSelecionado'):
            order.freteValue = params['freteSelecionado']

        order.save()
        return order
    