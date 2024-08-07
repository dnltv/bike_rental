import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from .rentals.models import Bike, Rental

User = get_user_model()


@pytest.fixture
def user():
    return User.objects.create_user(
        username='testuser',
        email='testemail',
        password='testpassword'
    )
