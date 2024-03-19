from flask_restful import Resource
from flask import request
from firebase_admin import storage



class UploadHandler(Resource):
    def post(self):
        """Upload a new file"""
        try:
            filename = ''
            if 'file' in request.files:
                file = request.files['file']
                filename = file.filename

                bucket = storage.bucket()
                blob = bucket.blob(filename)
                blob.upload_from_string(file.read(), content_type=file.content_type)
                blob.make_public()
                # Obtém o URL de download do arquivo enviado
                download_url = blob.public_url
                print('\n\nURL Público:', download_url)
                print('\n\nblob', blob.__dict__)
            return {'path': download_url}

        except Exception as error:
            return{
                'message': 'Error on upload a file',
                'details': str(error)
            },500
