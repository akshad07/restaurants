
from django.urls import path
from .views import MarkersMapView

app_name = "restaurants"

urlpatterns = [
    path(
        "map/", MarkersMapView.as_view()
    ),
]