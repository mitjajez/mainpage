from django.contrib.auth import models as auth_models
from django.contrib.auth import backends as auth_backends
from django.contrib.sessions import models as sessions_models

import aprmd5
import crypt

class AprBackend(object):
    supports_object_permissions = False
    supports_anonymous_user = False
    supports_inactive_user = False

    def authenticate(self, username=None, password=None):
        """
        Authenticates against the database using Apache Portable Runtime MD5 hash function.
        """
        try:
            user = auth_models.User.objects.get(username=username)
            if aprmd5.password_validate(password, user.password):
                # Successfully checked password, so we change it to the Django password format
                user.set_password(password)
                user.save()
                return user
        except ValueError:
            return None
        except auth_models.User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        """
        Translates the user ID into the User object.
        """
        try:
            return auth_models.User.objects.get(pk=user_id)
        except auth_models.User.DoesNotExist:
            return None

class CryptBackend(object):
    supports_object_permissions = False
    supports_anonymous_user = False
    supports_inactive_user = False

    def authenticate(self, username=None, password=None):
        """
        Authenticates against the database using crypt hash function.
        """
        try:
            user = auth_models.User.objects.get(username=username)
            if crypt(password, user.password) == user.password:
                # Successfully checked password, so we change it to the Django password format
                user.set_password(password)
                user.save()
                return user
        except ValueError:
            return None
        except auth_models.User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        """
        Translates the user ID into the User object.
        """
        try:
            return auth_models.User.objects.get(pk=user_id)
        except auth_models.User.DoesNotExist:
            return None

class ModelBackend(auth_backends.ModelBackend):
    def authenticate(self, username=None, password=None):
        """
        Authenticates against the database using official implementation but catches exceptions.
        """
        try:
            return super(ModelBackend, self).authenticate(username, password)
        except ValueError:
            return None