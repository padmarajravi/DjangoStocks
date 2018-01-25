# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Company(models.Model):
    full_name    = models.TextField()

    def __str__(self):
        return self.full_name


class Stocks(models.Model):
    company      = models.ForeignKey(Company,on_delete=models.CASCADE)
    date         = models.DateField(null=True)
    open         = models.FloatField(null=True)
    high         = models.FloatField(null=True)
    low          = models.FloatField(null=True)
    close        = models.FloatField(null=True)
    trade_value  = models.FloatField(null=True)
    trade_volume = models.FloatField(null=True)

    def __str__(self):
        return self.company.full_name +":"+ str(self.close)


class Relationship(models.Model) :
    relationship_name = models.TextField(null=True)

    def __str__(self):
        return self.relationship_name


class Relationships(models.Model):
    company1     = models.ForeignKey(Company,related_name="company1")
    relationship = models.ForeignKey(Relationship)
    company2     = models.ForeignKey(Company,related_name="company2")

    def __str__(self):
        return self.relationship

# Create your models here.
