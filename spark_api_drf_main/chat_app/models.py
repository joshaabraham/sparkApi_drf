from django.db import models

# Create your models here.
class Chat(models.Model):
        dateCreation = models.DateTimeField(auto_now_add=True, null=False)
        dateMiseAJour = models.DateTimeField(auto_now=True, null=False)
