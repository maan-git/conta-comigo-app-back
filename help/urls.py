from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url
from help import views

app_name = 'help'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'helpcategory', views.HelpCategoryView)
router.register(r'helprequeststatus', views.HelpRequestStatusView)
router.register(r'helpingstatus', views.HelpingStatusView)
router.register(r'helprequest', views.HelpRequestView)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls))
]
