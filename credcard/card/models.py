from django.db import models
from django.contrib.auth import get_user_model


class Card(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    score = models.IntegerField()
    credit = models.FloatField()
    status = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True, db_index=True)
