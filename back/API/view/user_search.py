from flask_restful import Resource
from flask import request
from models.user import User


class UsersSearchHandler(Resource):
    """Users Search Handler"""
    def get(self):
        """Get Users"""
        try:
            users = User.search(request.args.get('name'))
            response = {
                'users': []
            }

            for user in users:
                response['users'].append(user.to_dict())
            if response['users']:    
                return response['users']
            return response

        except Exception as error:
            return {
                       'message': 'Bad request, param name is required'
                   }, 500
