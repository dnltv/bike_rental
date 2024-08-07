from rest_framework.viewsets import ModelViewSet
from .models import Bike, Rental
from .serializers import BikeSerializer, RentalSerializer


class BikeViewSet(ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer


class RentalViewSet(ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
