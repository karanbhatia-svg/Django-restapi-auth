from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, validate_email
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]+$',
                message='Username must consist of letters only.',
            ),
        ]
    )
    name = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z\\s]+$',
                message='Name must consist of letters and spaces only.',
            ),
        ]
    )
    password = models.CharField(
        max_length=128,
        validators=[
            RegexValidator(
                regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*#?&])[A-Za-z\\d@$!%*#?&]{8,}$',
                message='Password must contain at least 8 characters, including at least 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special character.',
            ),
        ]
    )
    mobile = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[0-9]{10}$',
                message='Mobile number must be 10 digits.',
            ),
        ]
    )

    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True, validators=[validate_email])

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'mobile', 'address', 'email']
