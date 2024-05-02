from flask_restful import Resource
from flask import request
from models.order import Order
from modules.order import OrderModule


class OrderHandler(Resource):

    def post(self, order_id=None):
        """Create or update an order"""
        try:
            if not request.json:
                return {"message": "Bad request, no params for order"}, 400
            
            if order_id:
                order = Order.get_order(order_id)
                if not order:
                    return {"message": f"Order with id {order_id} not found"}, 404
                
                order_update = OrderModule.update(request.json, order)
                return order_update.to_dict()
            
            else:
                new_order = OrderModule.create(request.json)
                return new_order.to_dict()

        except Exception as error:
            return {
                'message': 'Error creating or updating an order',
                'details': str(error)
            }, 500
        

    def get(self):
        """Get Order"""
        try:
            order = Order.get_order()
            if order:
                return order.to_dict()
            return {}
        except Exception as error:
            return {
                'message': 'Error on get order',
                'details': str(error)
            }, 500