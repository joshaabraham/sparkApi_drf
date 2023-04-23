from rest_framework import generics
from publicite_app.models import AdCampaign, Ad
from .serializers import AdCampaignSerializer, AdSerializer

class AdCampaignListCreateView(generics.ListCreateAPIView):
    queryset = AdCampaign.objects.all()
    serializer_class = AdCampaignSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AdCampaignRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdCampaign.objects.all()
    serializer_class = AdCampaignSerializer

class AdListCreateView(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

class AdRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer