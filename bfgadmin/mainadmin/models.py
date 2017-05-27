from django.db import models
from django.contrib.auth.models import User

"""-------------------------------- Categories Model -------------------------------------------"""

"""
Custom Manadger for model Categories
"""

class ManadgerCategories(models.Manager):
#Get active Categories
    def get_active_categories(self):
        return self.get_queryset().filter(is_active__exact = True)

#Get categories on 5 ps.
    def get_list_categories(self):
        activecategories = self.get_active_categories()
        return [activecategories[i:i+5] for i in range(0, len(activecategories), 5)]


class Categories(models.Model):
    name = models.CharField(max_length=50)
    link_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    icon_style = models.CharField(max_length=50, default='')
    is_icon_img = models.BooleanField(default=False)
    max_num = models.SmallIntegerField(default=1)
    paid_num = models.SmallIntegerField(default=5)
    object = ManadgerCategories()

    class Meta:
        db_table = 'mainbfg_categories'

    def get_absolute_url(self):
        return "/categories/%s/" % self.link_name

    def __str__(self):
        return self.name


"""-------------------------------- Regions Model -------------------------------------------"""
class ManadgerRegions(models.Manager):
    pass

class Regions(models.Model):
    name = models.CharField(max_length=100)
    link_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    object = ManadgerRegions()

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