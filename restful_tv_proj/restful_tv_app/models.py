from django.db import models
from django.db.models.fields import CharField, DateTimeField

class TV_Show_Manager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['title']) <= 2:
            errors["title"] = "Title should be at leased 2 characters."
        if len(post_data['desc']) <= 10:
            errors["desc"] = "Desc should be at leased 10 characters."
        return errors

class Network_Manager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        
        return errors

class Network(models.Model):
    name = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class TV_Show(models.Model):
    title = models.CharField(max_length=255)
    networks = models.ManyToManyField(Network, related_name="shows")
    release_date = models.DateField()
    desc = models.TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    objects = TV_Show_Manager()
