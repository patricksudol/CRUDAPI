import uuid

from django.utils import timezone

from django.db import models


class Widget(models.Model):
    """
    A model representing a Widget or component of a HTML page.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=64)

    number_of_parts = models.IntegerField()

    created_date = models.DateTimeField(default=timezone.now)

    updated_date = models.DateTimeField(auto_now=True)
