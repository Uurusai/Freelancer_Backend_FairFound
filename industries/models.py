import uuid
from django.db import models

class Industry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    features = models.JSONField(default=list)

    def __str__(self):
        return self.name
