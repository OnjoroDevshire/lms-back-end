from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('learner', 'Learner'),
        ('tutor', 'Tutor'),
    )

    user_type = models.CharField(max_length=7, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.username

