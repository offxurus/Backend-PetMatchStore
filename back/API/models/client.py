"""Client model"""

import uuid


from modules.main import MainModule

class Client(object):
    """Client"""

    _collection_name = 'Client'

    def __init__(self, **args):
        self.id = args.get('id', uuid.uuid4().hex)
        self.cpf = args.get('cpf')
        self.name = args.get('name')
        self.birth_date = args.get('birth_date')
        self.gender = args.get('gender')
        self.email = args.get('email')
        self.password = args.get('password')
        self.billing_address = args.get('billing_address')
        self.group = args.get('group')
        self.active = args.get('active')
        self.delivery_address = args.get('delivery_address', []) 

    def save(self):
        """Save Client"""
        MainModule.get_firestore_db().collection(
            self._collection_name).document(self.id).set(self.to_dict())
        
    def to_dict(self):
        """Transform user in dict format"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'cpf': self.cpf,
            'group': self.group,
            'active': self.active,
            'gender': self.gender,
            'birth_date': self.birth_date,
            'billing_address': self.billing_address,
            'delivery_address': self.delivery_address
        }
    
    @classmethod
    def get_client(cls, client_id):
        """Get Client"""
        client = MainModule.get_firestore_db().collection(
            cls._collection_name).document(client_id).get()
        if client.exists:
            return Client(**client.to_dict())
        return None
    
    @classmethod
    def get_client_by_email(cls, email):
        """Get Client by params"""
        client = MainModule.get_firestore_db().collection(
            cls._collection_name).where(u'email', u'==', email).stream()
        return client