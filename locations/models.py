from django.db import models


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    country = models.ForeignKey(to=Country, related_name='states')


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    pib = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    state = models.ForeignKey(to=State, related_name='cities')
