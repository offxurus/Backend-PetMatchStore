""" User Module """
from models.client import Client
from modules.utils import encripty


class ClientModule(object):
    """Client module"""

    @staticmethod
    def create(params):
        """
        Create new client
        :param params: client dict
        return client: Client
        """

        client = Client()
        client.name = params['name']
        client.email = params['email']
        client.cpf = params['cpf']
        client.group = params['group']
        client.active = True
        client.birth_date = params['birth_date']
        client.gender = params['gender']
        client.billing_address = params['billing_address']
        client.delivery_address = params['delivery_address']

        password_json = {'password': params['password']}
        enc_password = encripty(password_json)
        client.password = enc_password

        client.save()
        return client
    
    @staticmethod
    def update(params, client):
        """
        Update client
        :param params: client dict
        return client: Client
        """

        if params.get('name'):
            client.name = params['name']
        if params.get('cpf'):
            client.cpf = params['cpf']
        if params.get('group'):
            client.group = params['group']
        if params.get('password'):
            password_json = {'password': params['password']}
            enc_password = encripty(password_json)
            client.password = enc_password
        if params.get('active') != None:
            client.active = params['active']
        if params.get('birth_date'):
            client.birth_date = params['birth_date']
        if params.get('gender'):
            client.gender = params['gender']
        if params.get('billing_address'):
            client.billing_address = params['billing_address']
        if params.get('delivery_address'):
            client.delivery_address = params['delivery_address']

        client.save()
        return client

        
        