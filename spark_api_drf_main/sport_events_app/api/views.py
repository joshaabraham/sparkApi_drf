from rest_framework import generics
from sport_events_app.models import SportEvent
from .serializers import SportEventSerializer

class SportEventListCreateView(generics.ListCreateAPIView):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SportEventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SportEvent.objects.all()
    serializer_class = SportEventSerializer