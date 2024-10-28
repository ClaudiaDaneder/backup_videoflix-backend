from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string

class Customer(AbstractUser):
    street = models.CharField(max_length=150, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    notes = models.TextField(max_length=1500, blank=True, null=True)
    activation_token = models.CharField(max_length=40, blank=True, null=True)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    activation_token = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.username


    def generate_activation_token(self):
        self.activation_token = get_random_string(length=40)
        self.save()
