""" User Module """
from models.user import User
from modules.utils import encripty


class UserModule(object):
    """User module"""

    @staticmethod
    def create(params):
        """
        Create new user
        :param params: user dict
        return user: User
        """
        user = User()
        user.name = params['name']
        user.email = params['email']
        user.cpf = params['cpf']
        user.group = params['group']
        user.active = True

        password_json = {'password': params['password']}
        enc_password = encripty(password_json)
        user.password = enc_password

        user.save()
        return user
    
    @staticmethod
    def update(params, user):
        """
        Update user
        :param params: user dict
        return user: User
        """

        if params.get('name'):
            user.name = params['name']
        if params.get('cpf'):
            user.cpf = params['cpf']
        if params.get('group'):
            user.group = params['group']
        if params.get('password'):
            password_json = {'password': params['password']}
            enc_password = encripty(password_json)
            user.password = enc_password
        if params.get('active') != None:
            user.active = params['active']

        user.save()
        return user
    


