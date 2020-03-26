from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from django.conf.urls import include

from .views.login_view import LoginView
from .views.logout_view import LogoutView
from .views.user_view import UserView
from .views.city_view import CityView

router = DefaultRouter()
router.register(r'user', UserView)
router.register(r'city', CityView)

app_name = 'app'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/', LoginView.as_view()),
    url(r'^logout/', LogoutView.as_view())
]
