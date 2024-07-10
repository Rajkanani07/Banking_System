from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

# define the router path and viewset to be used
# router.register(r'geeks', GeeksViewSet)

# specify URL Path for rest_framework
urlpatterns = [
    path("", include(router.urls)),
]
