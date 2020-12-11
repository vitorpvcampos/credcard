from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from credcard.base.views import UserViewSet
from credcard.card.views import CardViewSet

router = routers.DefaultRouter()
router.register(r'cards', CardViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
]
