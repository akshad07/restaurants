
from django.contrib.gis import admin
from .models import Restaurant


@admin.register(Restaurant)
class MarkerAdmin(admin.GISModelAdmin):
    list_display = ("name", "opentime", "address", "location")