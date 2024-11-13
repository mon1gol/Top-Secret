from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'user'