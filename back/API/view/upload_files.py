import uuid
from flask_restful import Resource
from flask import request
from firebase_admin import storage
from models.products import Products





class UploadHandler(Resource):
    def post(self):
        """Upload a new file"""
        try:
            product_id = (request.args.get('productId'))
            product = Products.get_product(product_id)
            filename = ''
            if 'file' in request.files:
                file = request.files['file']
                filename = f'{str(uuid.uuid4().hex)}.{file.filename.split('.')[-1]}'
                file.content_type

                bucket = storage.bucket()
                blob = bucket.blob(filename)
                blob.upload_from_string(file.read(), content_type=file.content_type)
                blob.make_public()
                # Obtém o URL de download do arquivo enviado
                download_url = blob.public_url
                product.images.append(download_url)
                product.save()
            return {'path': download_url}

        except Exception as error:
            return{
                'message': 'Error on upload a file',
                'details': str(error)
            },500
