from django.db import models

# Create your models here.

class User(models.Model):
        firstname = models.CharField(max_length=255, blank=False)
        lastname = models.CharField(max_length=255, blank=False)
        description = models.TextField(max_length=255)
        password = models.CharField(max_length=255, blank=False)
        age = models.IntegerField(null=True, blank=True)
        email = models.EmailField()

        profilPicture = models.ImageField()
        headerPagePicture = models.ImageField()

        dateCreation = models.DateTimeField(auto_now_add=True, null=False)
        dateMiseAJour = models.DateTimeField(auto_now=True, null=False)


        def __str__(self):
                return self.firstname + " " + self.lastname