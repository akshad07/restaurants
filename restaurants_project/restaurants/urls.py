
from django.urls import path
from .views import RestaurantsListview, RestaurantCreateView, RestaurantMapView
app_name = "restaurants"

urlpatterns = [
    # path(
    #     "map/", MarkersMapView.as_view(),
    #     name="map"
    # ),
    path(
        "", RestaurantsListview.as_view(),
        name="restaurants_list"
    ),
    path('create/', RestaurantCreateView.as_view(), name='create_restaurant'),
    path('map/', RestaurantMapView.as_view(), name='map'),
]