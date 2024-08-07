from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Bike, Rental
from .serializers import BikeSerializer, RentalSerializer


class BikeViewSet(ModelViewSet):
    queryset = Bike.objects.filter(is_available=True)
    serializer_class = BikeSerializer


class RentalViewSet(ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def get_queryset(self):
        return Rental.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def end_rental(self, request, pk=None):
        rental = self.get_object()
        rental.end_time = timezone.now()
        rental.save()
        return Response({'status': 'rental ended.'})

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
