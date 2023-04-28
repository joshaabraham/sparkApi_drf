from django.db import models

# Create your models here.
class Contact(models.Model):
    dateCreation = models.DateTimeField(auto_now_add=True, null=False)
    dateMiseAJour = models.DateTimeField(auto_now=True, null=False)


# Relations et interactions:

#     Liste d'amis / abonnés / abonnements
#     Groupes et communautés
#     Interactions avec les publications (likes, commentaires, partages)
#     Messages privés
#     Mentions et tags