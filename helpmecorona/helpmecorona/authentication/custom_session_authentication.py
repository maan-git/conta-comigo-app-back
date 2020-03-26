from rest_framework.authentication import SessionAuthentication


class CustomSessionAuthentication(SessionAuthentication):
    """
    Use Django's session framework for authentication.
    """

    def enforce_csrf(self, request):
        """
        Remove CSRF validation for session based authentication.
        """
        pass
