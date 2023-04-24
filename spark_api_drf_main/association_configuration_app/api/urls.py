from django.urls import path
from association_configuration_app.api.views import views

urlpatterns = [
    path("sports_association_configurations/", views.SportsAssociationConfigurationListCreateView.as_view(), name="sports_association_configuration_list_create"),
    path("sports_association_configurations/<int:pk>/", views.SportsAssociationConfigurationRetrieveUpdateDestroyView.as_view(), name="sports_association_configuration_detail"),
]