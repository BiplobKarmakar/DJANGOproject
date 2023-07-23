from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    status_choices = (
        ('Choices', 'Choices'),
        ('Buyer', 'Buyer'),
        ('Seller', 'Seller'),
    )

    status = models.CharField(
        max_length=20, choices=status_choices, default='choices')
    #choices =  User. forms.ChoiceField(choices=GENDER_CHOICES)

    


# Create your models here.
