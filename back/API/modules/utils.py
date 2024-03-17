""" Utils """
import jwt
from modules.main import SECRET_KEY


def encripty(payload):
    """ Encripty password """
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return token

def decrypt(token):
    """ decrypt password """
    dec_password = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

    return dec_password['password']
