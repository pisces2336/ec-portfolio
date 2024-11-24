from core.models import BaseModel
from django.db import models


class Item(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()

    class Meta:
        db_table = "item"
