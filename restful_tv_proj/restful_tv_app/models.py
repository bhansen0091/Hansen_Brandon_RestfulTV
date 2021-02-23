from django.db import models
from django.db.models.fields import CharField, DateTimeField

class Network(models.Model):
    name = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class TVShow(models.Model):
    title = models.CharField(max_length=255)
    networks = models.ManyToManyField(Network, related_name="shows")
    release_date = models.DateField()

