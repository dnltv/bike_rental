from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.views import UserCreate

from .views import BikeViewSet, RentalViewSet

app_name = 'rentals'

router_v1 = DefaultRouter()
router_v1.register(r'bikes', BikeViewSet, 'bikes')
router_v1.register(r'rentals', RentalViewSet, 'rentals')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreate.as_view(), name='register'),
    path('', include(router_v1.urls)),
]
