from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url

router = DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
]
