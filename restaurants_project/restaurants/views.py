from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView
from .models import Restaurant
from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize
from django.urls import reverse_lazy


class RestaurantsListview(ListView):
    """
    View for listing all restaurants.
    Uses ListView to display a list of restaurants.
    """
    model = Restaurant
    template_name = "dashboard/restaurants_list.html"
    context_object_name = "restaurants"


class RestaurantCreateView(CreateView):
    """
    View for creating a new restaurant.
    Uses CreateView to handle form submission and create a new restaurant instance.
    """
    model = Restaurant
    template_name = 'dashboard/restaurant_add.html'
    fields = ['name', 'opentime', 'address']  # Exclude location field as it will be handled separately

    def form_valid(self, form):
        """
        Override form_valid to handle location data separately and set it in the form instance.
        """
        latitude = self.request.POST.get('latitude')
        longitude = self.request.POST.get('longitude')
        location = f"POINT({longitude} {latitude})"
        
        # Set location in form instance
        form.instance.location = location
        
        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to the restaurants list view after successful form submission.
        """
        return reverse_lazy('restaurants:restaurants_list')


class RestaurantMapView(TemplateView):
    """
    View for displaying a map with restaurant locations.
    Uses TemplateView to render a template containing a map.
    """
    template_name = "dashboard/restaurant_map.html"

    def get_context_data(self, **kwargs):
        """
        Override get_context_data to provide additional context data for the template.
        Serializes restaurant locations and prepares restaurant data for the map.
        """
        context = super().get_context_data(**kwargs)
        
        # Serialize Restaurant locations as GeoJSON
        context['restaurants'] = serialize("geojson", Restaurant.objects.all(),
                                           geometry_field="location", fields=["name", "opentime", "address"])
        
        # Prepare restaurant data for map markers
        restaurant_data = []
        for restaurant in Restaurant.objects.all():
            point = GEOSGeometry(restaurant.location.wkb)
            lat, lon = point.y, point.x
            restaurant_data.append({
                'lat': lat,
                'lon': lon,
                'name': restaurant.name,
                'opentime': restaurant.opentime.strftime('%H:%M:%S'),
                'address': restaurant.address
            })
        
        context['restaurant_data'] = restaurant_data
        return context
