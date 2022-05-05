import dateutil.utils
from django.db import models
from datetime import datetime
from random import random, randint

# Create your models here.
# for database


class AdminInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class IndividualInfo(models.Model):
    username = models.CharField(verbose_name="username", max_length=32,
                                default=(datetime.strftime(datetime.now(), '%Y%m%d%H%M')) + str(randint(1000, 9999)))
    password = models.CharField(verbose_name="password", max_length=64,
                                default=(datetime.strftime(datetime.now(), '%Y%m%d%H%M')) + str(randint(1000, 9999)))
    street = models.CharField(verbose_name="street", max_length=64)
    city = models.CharField(verbose_name="city", max_length=32)
    zipcode = models.CharField(verbose_name="zipcode", max_length=10)
    email = models.CharField(verbose_name="e-mail address", max_length=32)
    phone = models.CharField(verbose_name="phone number", max_length=32)
    FirstName = models.CharField(verbose_name="first name", max_length=32)
    MiddleName = models.CharField(verbose_name="middle name", max_length=32)
    LastName = models.CharField(verbose_name="last name", max_length=32)
    InsuranceCompany = models.CharField(verbose_name="insurance company", max_length=32)
    InsuranceNumber = models.CharField(verbose_name="insurance number", max_length=10)
    rate = models.DecimalField(verbose_name="Coupon Rate", max_digits=10, decimal_places=2, default=0)
    StartDate = models.DateField(verbose_name="Start Date")
    EndDate = models.DateField(verbose_name="End Date")


class CorporationUser(models.Model):
    street = models.CharField(verbose_name="street", max_length=64)
    city = models.CharField(verbose_name="city", max_length=32)
    zipcode = models.CharField(verbose_name="zipcode", max_length=10)
    email = models.CharField(verbose_name="e-mail address", max_length=32)
    phone = models.CharField(verbose_name="phone number", max_length=32)
    employ_id = models.CharField(verbose_name="employ id", max_length=10)
    corporation_choices = (
        (1, "D&G Tax Law"),
        (2, "The Acrobatic Accountants LLC"),
        (3, "Cafe Msica"),
        (4, "Artisan Recording"),
        (5, "New York Man"),
        (6, "Dreamlike Moustaches"),
        (7, "Swift River Sports"),
        (8, "The Big Apple Cocktail Company"),
        (9, "Pouring Palaces"),
        (10, "Schmalzy Pet"),
    )
    corporation_name = models.SmallIntegerField(verbose_name="corporation name", choices=corporation_choices)
    rate = models.DecimalField(verbose_name="Coupon Rate", max_digits=10, decimal_places=2, default=0)


class Admin(models.Model):
    username = models.CharField(verbose_name="user name", max_length=32)
    password = models.CharField(verbose_name="password", max_length=64)


class Office(models.Model):
    name = models.CharField(verbose_name="office name", max_length=64)
    street = models.CharField(verbose_name="street", max_length=64)
    city = models.CharField(verbose_name="city",max_length=32)
    zipcode = models.CharField(verbose_name="zipcode", max_length=10)
    phone = models.CharField(verbose_name="phone number", max_length=10)
