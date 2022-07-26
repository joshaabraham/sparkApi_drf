import code
from django.db import models

# Create your models here.

class Sport(models.Model):
        code = models.CharField(max_length=4)
        titre = models.CharField(max_length=150)
        categorie = models.CharField(max_length=150)
        icon_petit = models.ImageField(max_length=150)
        icon_grand = models.ImageField(max_length=150)

        dateCreation = models.DateTimeField(auto_now_add=True, null=False)
        dateMiseAJour = models.DateTimeField(auto_now=True, null=False)
