from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    personal_number = models.CharField(max_length=11)
    last_name = models.CharField(max_length=30)
    adress  = models.CharField(max_length=300)
    #phone_number = models.CharField(max_length=30)


def __unicode__(self):
    return self.personal_number
def __str__(self):
    return self.personal_number
##class Job(model.Model):
##    name_job = models.Charfield (max_length=30)
##    reward = models.DecimalField(max_digits=100,decimal_places=2)

#def __str__(self):
#    return self.name_job
