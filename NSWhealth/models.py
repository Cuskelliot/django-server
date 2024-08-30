from django.db import models

class Patient(models.Model):
    MRN = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    DOB = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    suburb = models.CharField(max_length=50)
    postcode = models.CharField(max_length=4)
    state = models.CharField(max_length=3)
    country = models.CharField(max_length=15)


class Staff(models.Model):
    staff_ID = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
