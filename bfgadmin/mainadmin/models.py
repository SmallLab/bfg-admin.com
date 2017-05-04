from django.db import models

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
