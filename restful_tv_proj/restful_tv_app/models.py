from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.http import request
import datetime

class TV_Show_Manager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['title']) <= 2:
            errors["title"] = "Title should be at leased 2 characters."
        if len(post_data['desc']) <= 10:
            errors["desc"] = "Desc should be at leased 10 characters." 

        if len(post_data['release_date']) != 10:
            errors['invalid_date'] = "Invalid Date"
        else:
            rd_convert = datetime.datetime.strptime(post_data['release_date'], "%Y-%m-%d")

            if rd_convert > datetime.datetime.today():
                errors['release_data_invalid'] = "The release date is not in the past."

        return errors


class Network_Manager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['add_new_network']) < 3:
            errors["name_short"] = "Network name must be at leased 3 characters in length."
        
        return errors

class Network(models.Model):
    name = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    objects = Network_Manager()

class TV_Show(models.Model):
    title = models.CharField(max_length=255)
    networks = models.ManyToManyField(Network, related_name="shows")
    release_date = models.DateField()
    desc = models.TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    objects = TV_Show_Manager()
