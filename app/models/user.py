from django.db import models as django_models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from simple_history.models import HistoricalRecords
from app.models.user_address import UserAddress
from utils.models_validations import validate_phone
from utils.models_validations import validate_cpf
from django.db.models.signals import pre_save
from django.dispatch import receiver


DEFAULT_USER_IMAGE_URL = "https://firebasestorage.googleapis.com/v0/b/conta-comigo-app-files.appspot.com/o/icon-conta-comigo.jpeg?alt=media&token=0094390a-0f27-4735-a0be-5926c5302b6e"


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
    avatar = django_models.URLField(_("Avatar"), default=DEFAULT_USER_IMAGE_URL)
    is_superuser = django_models.BooleanField(_("Super user"), default=True)
    addresses = django_models.ManyToManyField(UserAddress, related_query_name="user")
    cpf = django_models.CharField(_("CPF"), max_length=11, validators=[validate_cpf])
    birth_date = django_models.DateField(_("Data de nascimento"))
    phone_number = django_models.CharField(
        _("Telefone"), max_length=14, validators=[validate_phone]
    )
    is_phone_whatsapp = django_models.BooleanField(_("Telefone é whatsapp"))
    is_at_risk_group = django_models.BooleanField(_("É do grupo de risco"))
    live_alone = django_models.BooleanField(_("Mora sozinho"))
    history = HistoricalRecords()

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

    # Check if will be needed to be implemented
    # @property
    # def is_anonymous(self):
    #     return True

    @property
    def is_staff(self):
        # TODO Improve validations to allow non superusers to log-in into admin interface
        return self.is_superuser

    @property
    def is_admin(self):
        return self.is_superuser

    def has_module_perms(self, app_label):
        # TODO Implement
        return False

    def has_perm(self, perm, obj=None):
        # TODO Implement
        return True


@receiver(pre_save, sender=User)
def pre_save(sender, instance: User, **kwargs):
    if instance.avatar is None:
        instance.avatar = DEFAULT_USER_IMAGE_URL
