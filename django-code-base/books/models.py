from django.db import models

# Create your models here.
from django.utils import timezone
import uuid

class Books(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField("Name", max_length=40)