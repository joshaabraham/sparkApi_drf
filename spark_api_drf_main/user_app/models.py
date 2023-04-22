from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email can not be null.')        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
        
        username = None
        email = models.EmailField(verbose_name='email address', unique=True) 
        lastname = models.CharField(max_length=255, blank=False)
        description = models.TextField(max_length=255)
        password = models.CharField(max_length=255, blank=False)
        age = models.IntegerField(null=True, blank=True)

        profilPicture = models.ImageField(blank=True)
        headerPagePicture = models.ImageField(blank=True)

        dateCreation = models.DateTimeField(auto_now_add=True, null=False)
        dateMiseAJour = models.DateTimeField(auto_now=True, null=False)

        objects = CustomUserManager()
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = []

        def __str__(self):
                return self.firstname + " " + self.lastname