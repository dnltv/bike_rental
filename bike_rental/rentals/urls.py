from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bike_rental.rentals.views import BikeViewSet, RentalViewSet

app_name = 'rentals'

router_v1 = DefaultRouter()
router_v1.register(r'bikes', BikeViewSet, 'bikes')
router_v1.register(r'rentals', RentalViewSet, 'rentals')

urlpatterns = [
    path('', include(router_v1.urls)),
]
