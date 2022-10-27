from email.policy import default
from random import choices
from django.db import models
import uuid
# Create your models here.


class Donor(models.Model):
    choices = (
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O', 'O'),
    )
    ch = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=3, choices=choices, default='A+')
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=200)
    dibetis = models.CharField(max_length=3, choices=ch, default='No')
    heart_deases = models.CharField(max_length=3, choices=ch, default='No')
    last_time_donated = models.DateField(default='2021-01-01')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-last_time_donated']


class Camp(models.Model):
    choices = (
        ('comming', 'comming'),
        ('closed', 'closed'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=300)
    date = models.DateField()
    time = models.TimeField()
    held = models.CharField(max_length=10, choices=choices, default="comming")

    def __str__(self):
        return self.name
