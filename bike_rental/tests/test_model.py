import pytest
from bike_rental.rentals.models import Bike, Rental


@pytest.mark.django_db
def test_bike_creation():
    bike = Bike.objects.create(name='Test bike')
    assert bike.name == 'Test bike'


@pytest.mark.django_db
def test_rental_creation(user, bike):
    rental = Rental.objects.create(user=user, bike=bike)
    assert rental.user == user
    assert rental.bike == bike
