from __future__ import unicode_literals

from django.db import models


class BookingAdd(models.Model):
    booking_type = models.CharField(max_length=255)
    description = models.TextField()
    persons = models.IntegerField()
    price = models.IntegerField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_info = models.TextField()
