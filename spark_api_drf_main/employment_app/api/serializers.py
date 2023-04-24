from rest_framework import serializers
from employment_app.models import JobOffer, JobSearch

class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = ["id", "title", "description", "location", "company", "posted_by", "posted_at", "updated_at"]

class JobSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSearch
        fields = ["id", "title", "description", "location", "searcher", "posted_at", "updated_at"]