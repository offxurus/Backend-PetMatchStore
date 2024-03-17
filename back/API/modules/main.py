"""Main module"""
from firebase_admin import firestore

SECRET_KEY = 'BATATA12'


class MainModule(object):
    """Main module"""

    @staticmethod
    def get_firestore_db():
        """Get firestore db instance"""
        return firestore.client()

