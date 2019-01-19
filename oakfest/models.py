from django.db import models
from django.contrib.auth.models import AbstractUser
from . import settings


class User(AbstractUser):

    class Meta:
        verbose_name_plural = "Company"

    company_name = models.CharField(max_length = 30)



    def __str__(self):
        return self.company_name

class Site(models.Model):

    class Meta:
        verbose_name = "Site"

    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = None, null = True)
    site_name = models.CharField(max_length = 30)
    city_name = models.CharField(max_length=30)
    ZIP_code = models.IntegerField()
    country_code = models.CharField(help_text="US, IN,..", max_length = 2)
    budget = models.IntegerField()
    area = models.DecimalField(help_text="In Square Meters", max_digits=30, decimal_places= 5)
    power_req = models.DecimalField(help_text="In Watts", max_digits=30, decimal_places= 5)

    def __str__(self):
        return self.site_name


