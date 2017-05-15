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



#-------------------------------- Profile Model -------------------------------------------#

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