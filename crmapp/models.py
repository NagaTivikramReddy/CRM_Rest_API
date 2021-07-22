from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


user = get_user_model()


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    course_interest = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now=True)
    claimed_by = models.ForeignKey(
        user, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='userenqueries')

    class Meta:
        verbose_name = 'Enquirie'

    def __str__(self):
        return self.course_interest

    def claim(self, request):

        self.claimed_by = request.user
        self.save()

    def get_absolute_url(self):
        return reverse('index')
