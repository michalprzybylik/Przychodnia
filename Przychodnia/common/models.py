from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('REJ', 'REJESTRATORKA'),
        ('LEK', 'LEKARZ'),
    )
    role = models.CharField(null=True, max_length=16, choices=ROLES)
