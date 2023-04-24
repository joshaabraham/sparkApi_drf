from rest_framework import serializers
from sport_events_app.models import SportEvent
from user_app.api.serializers import UserSerializer

class SportEventSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = SportEvent
        fields = ["id", "user", "name", "description", "location", "event_date"]