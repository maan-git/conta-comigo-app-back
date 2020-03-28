from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = django_models.EmailField(_("email address"), unique=True)
    first_name = django_models.CharField(_("first name"), max_length=30, blank=True)
    last_name = django_models.CharField(_("last name"), max_length=30, blank=True)
    date_joined = django_models.DateTimeField(_("date joined"), auto_now_add=True)
    is_active = django_models.BooleanField(_("active"), default=True)
    avatar = django_models.ImageField(upload_to="avatars/", null=True, blank=True)
    is_superuser = django_models.BooleanField(_("Super user"), default=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.email

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    # @AbstractBaseUser.is_active
    # def is_active(self):
    #     return True

    # @property
    # def is_anonymous(self):
    #     return True
    #
    # @property
    # def is_authenticated(self):
    #     return True

    @property
    def is_staff(self):
        # TODO Check
        return True

    # @property
    # def is_admin(self):
    #     # TODO Check
    #     return True
    #
    def has_module_perms(self, app_label):
        # TODO Check
        return False

    def has_perm(self, perm, obj=None):
        # TODO Check
        return True

    # def check_password(self, raw_password):
    #     """
    #     Return a boolean of whether the raw_password was correct. Handles
    #     hashing formats behind the scenes.
    #     """
    #     user = authenticate_user_ldap(getattr(self, self.USERNAME_FIELD, None), raw_password)
    #
    #     return user is not None
    #
    # def set_password(self, password):
    #     pass
