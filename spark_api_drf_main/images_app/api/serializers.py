from rest_framework import serializers
from images_app.models import Album, Image
from user_app.api.serializers import UserSerializer

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "title", "description", "image", "album", "uploaded_at"]

class AlbumSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ["id", "title", "description", "owner", "images"]