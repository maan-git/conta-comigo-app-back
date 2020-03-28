from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from django.conf.urls import include

from .views.login_view import LoginView
from .views.logout_view import LogoutView
from .views.user_view import UserView
from .views.city_view import CityView
from .views.address_view import AddressView
from .views.zip_view import ZipView
from .views.neighborhood_view import NeighborhoodView
from .views.country_view import CountryView

router = DefaultRouter()
router.register(r"user", UserView)
router.register(r"city", CityView)
router.register(r"address", AddressView)
router.register(r"zip", ZipView)
router.register(r"neighborhood", NeighborhoodView)
router.register(r"country", CountryView)

app_name = "app"

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^login/", LoginView.as_view()),
    url(r"^logout/", LogoutView.as_view()),
]
