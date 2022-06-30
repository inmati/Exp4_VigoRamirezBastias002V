from datetime import date
from django.db import models

class Appointment(models.Model):

    email= models.CharField(verbose_name='email', primary_key=True, max_length=35, unique=True, null=False)
    first_name = models.CharField(verbose_name='first name', max_length=20, null=False)
    last_name = models.CharField(verbose_name='last name', max_length=20, null=False)
    phone = models.IntegerField(verbose_name='phone')
    address = models.CharField(verbose_name='address', max_length=50, null=False)
    date = models.CharField(verbose_name='date', max_length=10, null=False, default=None)

    def __repr__(self):
        return f'Appointment(email={self.email}, date={self.date})'
# Create your models here.
