from django.db import models
from django.conf import settings

class SportEvent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sport_events")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    event_date = models.DateTimeField()

    def __str__(self):
        return self.name