from flask_restful import Resource
from flask import request
from models.order import Order
from modules.order import OrderModule


class OrderHandler(Resource):

    def post(self):
        """Create an order"""
        try:
            if not request.json:
                return {"message": "Bad request, no params for order"}, 400
            
            new_order = OrderModule.create(request.json)

            return new_order.to_dict()

        except Exception as error:
            return {
                'message': 'Error creating an order',
                'details': str(error)
            }, 500
        

    def get(self, order_id = None):
        """Get Orders"""
        try:
            if not order_id:
                response = {"orders": []}
                orders = Order.get_order()
                for order in orders:
                    orders_json = order.to_dict()
                    response['orders'].append(orders_json)
                return response
            else:
                order = Order.get_order(order_id)
                if order:
                    return order.to_dict()
                else:
                    return {}
        except Exception as error:
            return {
                'message': 'Error on get order',
                'details': str(error)
            }, 500