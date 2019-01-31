from django.db import models
from django.utils import timezone
# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField("date published", default=timezone.now)

    def __str__(self):
        return self.title
