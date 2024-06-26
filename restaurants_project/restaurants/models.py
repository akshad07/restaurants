from django.db import models
from django.contrib.gis.db import models as gis_models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    opentime = models.TimeField()
    address = models.CharField(max_length=255)
    location = gis_models.PointField()

    def __str__(self):
        return self.name