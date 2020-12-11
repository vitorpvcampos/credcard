from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from credcard.base.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    user = get_user_model()
    queryset = user.objects.all()
    serializer_class = UserSerializer
