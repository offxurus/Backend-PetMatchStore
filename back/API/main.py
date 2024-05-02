"""Arquivo main da API"""
import firebase_admin
from firebase_admin import firestore, credentials

from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask_cors import CORS
from view.order import OrderHandler
from view.client import ClientsHandler, ClientHandler
from view.upload_files import UploadHandler
from view.user import UserHandler, UserSignInHandler, UsersHandler
from view.products import ProductsHandler, ProductHandler
from view.user_search import UsersSearchHandler

app = Flask(__name__)
CORS(app)
API = Api(app)

cred = credentials.Certificate(
    './petmatchstore-firebase-adminsdk-em0x5-7643a471fa.json')
##firebase_admin.initialize_app(credential=cred)
firebase_admin.initialize_app(cred, {
    'storageBucket': 'petmatchstore.appspot.com'
})

@app.before_request
def start_request():
    """Start api request"""
    if request.method == 'OPTIONS':
        return '', 200
    if not request.endpoint:
        return 'Sorry, Nothign at this URL.', 404


class Index(Resource):
    """ class return API index """

    def get(self):
        """return API"""
        return {"API": "PetMatchStore"}


API.add_resource(Index, '/', endpoint='index')
API.add_resource(UploadHandler, '/upload', endpoint='upload')
API.add_resource(UsersHandler, '/users', endpoint='users')
API.add_resource(UserHandler, '/user/<user_id>', endpoint='user')
API.add_resource(UserSignInHandler, '/user-sign-in', endpoint='user-sign-in')
API.add_resource(ProductsHandler, '/products', endpoint='products')
API.add_resource(ProductHandler, '/products/<product_id>', endpoint='product')
API.add_resource(UsersSearchHandler, '/search', endpoint='search')
API.add_resource(ClientsHandler, '/clients', endpoint='clients')
API.add_resource(ClientHandler, '/client/<client_id>', endpoint='client')
API.add_resource(OrderHandler, '/shopping-cart', endpoint='shopping-cart')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
