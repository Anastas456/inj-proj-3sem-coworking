from django.db import models
import jwt
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import coworking.settings as settings

class UserManager(BaseUserManager):
    def _create_user(self, email, username, first_name, last_name, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        try:
            user = self.model(email=email, username=username, first_name=first_name, last_name=last_name,  **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        except:
            raise
 
    def create_user(self, email, username, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, username, first_name, last_name, password, **extra_fields)
 
    def create_superuser(self, email, username, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
 
        return self._create_user(email, username, first_name, last_name, password=password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(username=username)

    # def create_user(self, username, email, first_name, last_name, password=None):
    #     if username is None:
    #         raise TypeError('Users must have a username.')

    #     if email is None:
    #         raise TypeError('Users must have an email address.')

    #     user = self.model(username=username, email=email, first_name=first_name, last_name=last_name)
    #     user.set_password(password)
    #     user.save()

    #     return user

    # def create_superuser(self, username, email, first_name, last_name, password):
    #     if password is None:
    #         raise TypeError('Superusers must have a password.')

    #     user = self.create_user(username, email, first_name, last_name, password)
    #     user.is_superuser = True
    #     user.is_staff = True
    #     user.save()

    #     return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username', 'first_name', 'last_name']

    objects = UserManager()

    # def __str__(self):
    #     return self.email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    @property
    def token(self):
        return self._generate_jwt_token()

    # def get_full_name(self):
    #     return self.first_name + self.last_name

    def get_username(self):
        return self.username

    def _generate_jwt_token(self):
    
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt,
            'username': self.username
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
