from django.contrib.gis.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    opentime = models.TimeField()
    address = models.CharField(max_length=255)
    location = models.PointField()

    def __str__(self):
        return self.name