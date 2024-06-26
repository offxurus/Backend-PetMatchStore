"""Users view"""
from flask_restful import Resource
from flask import request
from models.client import Client
from modules.utils import decrypt
from models.user import User

from modules.user import UserModule


class UsersHandler(Resource):
    """Users handler"""

    def get(self):
        """Get Users"""
        try:
            response = {"users": []}
            users = User.get_users()
            for user in users:
                users_json = user.to_dict()
                response['users'].append(users_json)
            for user_dict in response['users']:
                user_dict['password'] = decrypt(user_dict['password'])

            return response

        except Exception as error:
            return {
              'message': 'Error on get Users',
              'details': str(error)
            }, 500

    def post(self):
        """Create a new user"""
        try:
            request_params = request.json
            if not request.json:
                return {"message": "Bad request not params for user create"}, 400

            users = User.get_user_by_email(request_params['email'])
            for user in users:
                if user.to_dict():
                    return {"message": "E-mail already registered"}, 400

            user = UserModule.create(request_params)
            return user.to_dict()

        except Exception as error:
            return {
              'message': 'Error on create a new user',
              'details': str(error)

            }, 500
        
        
class UserHandler(Resource):
    """User handler"""

    def get(self, user_id):
        """Get User"""
        try:
            user = User.get_user(user_id)
            if user:
                return user.to_dict()
            return {}

        except Exception as error:
            return {
              'message': 'Error on get Users',
              'details': str(error)
            }, 500

    def post(self, user_id):
        """Update a user"""
        try:
            user = User.get_user(user_id)
            request_params = request.json
            if not request.json:
                return {"message": "Bad request not params for update user"}, 400
            if not user:
                return {"message": "user not found"}, 400
            UserModule.update(request_params, user)
            return user.to_dict()    

        except Exception as error:
            return {
              'message': 'Error on Update a user',
              'details': str(error)
            }, 500

class UserSignInHandler(Resource):
    """User Sign In handler"""

    def post(self):
        """Sign in User"""
        try:
            response = {}
            if not request.json:
                return {"message": "Bad request not params for user sign in"}, 400
            request_params = request.json
            if 'email' in request_params:
                clients = Client.get_client_by_email(request_params['email'])
                users = User.get_user_by_email(request_params['email'])
            else:
                return {"message": "Email is required"}, 400
            
            if(clients):
                for client in clients:
                    client = client.to_dict()
                    stored_password = client['password']
                    decrypted_stored_password = decrypt(stored_password) 
                    if decrypted_stored_password == request_params['password']:
                        response['id'] = client['id']
                        response['group'] = client['group']
                        response['active'] = client['active']
                        response['name'] = client['name']
                        response['birth_date'] = client['birth_date']
                        response['gender'] = client['gender']
                        response['billing_address'] = client['billing_address']
                        response['delivery_address'] = client['delivery_address']
                        response['cpf'] = client['cpf']
                        response['email'] = client['email']
                    response['password'] = decrypted_stored_password
                    return response
            
            for user in users:
                user = user.to_dict()
                stored_password = user['password']
                decrypted_stored_password = decrypt(stored_password) 
                if decrypted_stored_password == request_params['password']:
                    response['id'] = user['id']
                    response['group'] = user['group']
                    response['active'] = user['active']
                    response['name'] = user['name']
                    response['cpf'] = user['cpf']
                    response['email'] = user['email']
                response['password'] = decrypted_stored_password
            return response

        except Exception as error:
            return {
              'message': 'Error on get User',
              'details': str(error)
            }, 500
        
    
