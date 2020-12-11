from credcard.card.models import Card
from rest_framework.serializers import ModelSerializer


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'user', 'score', 'credit', 'status', 'created')
