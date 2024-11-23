import uuid

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db import models
from rest_framework.exceptions import NotFound

from .constants import ExceptionMessage


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def get_or_404(model: models.Model, **keywargs):
    try:
        return model.objects.get(**keywargs)
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        raise NotFound(ExceptionMessage.DoesNotExistsOrMultipleObjectsReturned)
