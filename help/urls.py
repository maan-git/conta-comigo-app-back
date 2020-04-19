from utils.views_utils import CustomRouterNoPut
from django.conf.urls import include, url
from help import views

app_name = "help"

# Create a router and register our viewsets with it.
router = CustomRouterNoPut()
router.register(r"helpcategory", views.HelpCategoryView, basename="helpcategory")
router.register(
    r"helprequeststatus", views.HelpRequestStatusView, basename="helprequeststatus"
)
router.register(r"helpingstatus", views.HelpingStatusView, basename="helpingstatus")
router.register(r"helprequest", views.HelpRequestView, basename="helprequest")
router.register(
    r"helprequestcancelreason",
    views.HelpRequestCancelReasonView,
    basename="helprequestcancelreason",
)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [url(r"^", include(router.urls))]
