from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bike_rental.rentals.views import BikeViewSet, RentalViewSet
from bike_rental.users.views import UserCreate

app_name = 'rentals'

router_v1 = DefaultRouter()
router_v1.register(r'bikes', BikeViewSet, 'bikes')
router_v1.register(r'rentals', RentalViewSet, 'rentals')

urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('', include(router_v1.urls)),
]
