""" Order Module """
from models.order import Order

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
        order.products_order = params['products_order']
        order.total_price = params['total_price']

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
        if params.get('total_price'):
            order.total_price = params['total_price']

        order.save()
        return order
    