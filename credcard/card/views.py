from credcard.card.models import Card
from credcard.base.serializers import UserSerializer
from credcard.card.serializers import CardSerializer
from random import randint
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


def get_credit(salary):
    score = randint(1, 999)
    credit = salary / 2 if salary / 2 > 1000 else 1000
    value = {'status': False, 'score': 1, 'credit': 0}
    dict_score = {
        299: {'status': False, 'score': score, 'credit': 0},
        599: {'status': True, 'score': score, 'credit': 1000},
        799: {'status': True, 'score': score, 'credit': credit},
        950: {'status': True, 'score': score, 'credit': 2 * salary},
        999: {'status': True, 'score': score, 'credit': 1000000},
    }

    for upper_bound, value in dict_score.items():
        if score <= upper_bound:
            break
    return value


class CardViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def create(self, request, *args, **kwargs):
        salary = UserSerializer(request.user).data['salary']
        card = Card.objects.create(**get_credit(salary), user=request.user)
        serializer = CardSerializer(card)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            cards = Card.objects.all()
        else:
            cards = Card.objects.filter(user=request.user)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)
