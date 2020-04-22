from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url
from notification.views.email_view import EmailView

router = DefaultRouter()
router.register(r'email', EmailView)

urlpatterns = [
    url(r'^', include(router.urls)),
]
