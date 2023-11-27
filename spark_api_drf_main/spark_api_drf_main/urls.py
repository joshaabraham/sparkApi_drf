"""spark_api_drf_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("abonnement_app.api.urls")),
    path("api/", include("academy_app.api.urls")),
    path("api/", include("association_app.api.urls")),
    path("api/", include("association_configuration_app.api.urls")),
    path("api/", include("chat_app.api.urls")),
    path("api/", include("contact_app.api.urls")),
    path("api/", include("comportement_app.api.urls")),
    path('api/', include('user_app.api.urls')),
    path("api/", include("ecommerce.api.urls")),
    path("api/", include("images_app.api.urls")),
    path("api/", include("equipe_app.api.urls")),
    path("api/", include("publicite_app.api.urls")),
    path("api/", include("abonnement_app.api.urls")),
    path("api/", include("localisation_app.api.urls")),
    path("api/", include("qr_codes_app.api.urls")),
    path("api/", include("user_config.api.urls")),
    path("api/", include("employment_app.api.urls")),
    # path("api/", include("service_app.api.urls")),
    path("api/", include("post_and_comment_app.api.urls")),
    path("api/", include("invitation_app.api.urls")),
    path("api/", include("interests_app.api.urls")),
    path("api/", include("user_app.api.urls")),
    
    
]
