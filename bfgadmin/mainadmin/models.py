from django.db import models
from django.contrib.auth.models import User

"""-------------------------------- Regions Model -------------------------------------------"""


class Regions(models.Model):
    name = models.CharField(max_length=100)
    link_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return "/%s/" % self.link_name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mainbfg_regions'


"""------------------------- TypeSentence Model -----------------------------------------------"""
"""
Custom Manadger for model TypeSentence
"""


class ManadgerTypeSentence(models.Manager):
#Get active Types
    def get_active_types(self):
        return self.get_queryset().filter(is_active__exact= True)


class TypeSentence(models.Model):
    name = models.CharField(max_length=50)
    link_name = models.CharField(max_length=50, default='')
    is_active = models.BooleanField(default=True)
    object = ManadgerTypeSentence()

    def get_absolute_url(self):
        return "/%s/" % self.link_name

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mainbfg_typesentence'

""""-------------------------------- Profile Model -------------------------------------------"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=100)
    email = models.EmailField(blank=True, max_length=255)
    favorite_num = models.SmallIntegerField(blank=True, default=0)
    is_subscrabtion = models.BooleanField(default=False)
    is_subscriber = models.BooleanField(default=False)
    facebook_id = models.BigIntegerField(blank=True, default=0)
    vk_id = models.IntegerField(blank=True, default=0)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'mainbfg_profile'