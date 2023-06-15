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
    path("abonnement_app/", include("abonnement_app.api.urls")),
    path("academy_app/", include("academy_app.api.urls")),
    path("association_app/", include("association_app.api.urls")),
    path("association_config/", include("association_configuration_app.api.urls")),
    path("chat/", include("chat_app.api.urls")),
    path("contact_app/", include("contact_app.api.urls")),
    path("comportement_app/", include("comportement_app.api.urls")),
    path('account/', include('user_app.api.urls')),
    path("ecommerce/", include("ecommerce.api.urls")),
    path("gallery/", include("images_app.api.urls")),
    path("equipe/", include("equipe_app.api.urls")),
    path("publicitee/", include("publicite_app.api.urls")),
    path("payment/", include("abonnement_app.api.urls")),
    path("localisation/", include("localisation_app.api.urls")),
    path("qrCodes/", include("qr_codes_app.api.urls")),
    path("user_config/", include("user_config.api.urls")),
    path("employment_app/", include("employment_app.api.urls")),
    # path("service_app/", include("service_app.api.urls")),
    path("post_and_comment_app/", include("post_and_comment_app.api.urls")),
    path("invitation_app/", include("invitation_app.api.urls")),
    path("interests_app/", include("interests_app.api.urls")),
    
    
]
