from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    founded = models.IntegerField()

    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    birthdate = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
