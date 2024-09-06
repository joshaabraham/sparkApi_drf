from rest_framework import serializers
from sport_app.api.serializers import SportSerializer
from sport_app.models import Sport
from sport_events_app.models import SportEvent
from user_app.api.serializers import UserSerializer

class SportEventSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    sport = SportSerializer(read_only=True)  # Utilise un serializer imbriqué pour afficher les détails de la catégorie
    sport_id = serializers.PrimaryKeyRelatedField(queryset=Sport.objects.all(), source='sport', write_only=True)  # Permet d'envoyer l'ID de la catégorie dans les requêtes


    class Meta:
        model = SportEvent
        fields = '__all__'
        
