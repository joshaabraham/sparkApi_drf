from rest_framework import serializers
from publicite_app.models import AdCampaign, Ad
from user_app.api.serializers import UserSerializer

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

class AdCampaignSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    ads = AdSerializer(many=True, read_only=True)

    class Meta:
        model = AdCampaign
        fields = '__all__'