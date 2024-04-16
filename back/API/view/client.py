"""Client view"""
from flask_restful import Resource
from flask import request
from modules.utils import decrypt
from models.client import Client

from modules.client import ClientModule

class ClientsHandler(Resource):
    """Client handler"""

    def post(self):
        """Create a new client"""
        try:
            request_params = request.json
            if not request.json:
                return {"message": "Bad request not params for client create"}, 400

            clients = Client.get_client_by_email(request_params['email'])
            for client in clients:
                if client.to_dict():
                    return {"message": "E-mail already registered"}, 400

            client = ClientModule.create(request_params)
            return client.to_dict()

        except Exception as error:
            return {
              'message': 'Error on create a new user',
              'details': str(error)

            }, 500
        
class ClientHandler(Resource):
    """Client handler"""

    def get(self, client_id):
        """Get Client"""
        try:
            client = Client.get_client(client_id)
            if client:
                return client.to_dict()
            return {}

        except Exception as error:
            return {
              'message': 'Error on get client',
              'details': str(error)
            }, 500
        
    def post(self, client_id):
        """Update a Client"""
        try:
            client = Client.get_client(client_id)
            request_params = request.json
            if not request.json:
                return {"message": "Bad request not params for update"}, 400
            if not client:
                return {"message": "client not found"}, 400
            ClientModule.update(request_params, client)
            return client.to_dict()    

        except Exception as error:
            return {
              'message': 'Error on Update infos',
              'details': str(error)
            }, 500