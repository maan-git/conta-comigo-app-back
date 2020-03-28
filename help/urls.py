from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url
from help.views.help_category_view import HelpCategoryView

app_name = "help"

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"helpcategory", HelpCategoryView)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r"^", include(router.urls)),
    # url(r'^login/', LoginView.as_view()),
    # url(r'^logout/', LogoutView.as_view())
]
