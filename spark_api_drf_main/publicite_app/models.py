from django.db import models
from django.conf import settings

class AdCampaign(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ad_campaigns")

    def __str__(self):
        return self.name

class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="ads/images/")
    url = models.URLField()
    ad_campaign = models.ForeignKey(AdCampaign, on_delete=models.CASCADE, related_name="ads")

    def __str__(self):
        return self.title