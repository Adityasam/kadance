from django.db import models
from django.urls import reverse
import datetime


# Create your models here.
class center(models.Model):
    center_id=models.PositiveIntegerField(default=None, null=True)
    name=models.CharField(max_length=100)
    allotted=models.PositiveIntegerField(default=None,null=True)
    date = models.DateField(default=datetime.date.today, null=True)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('main:detail', args=[self.center_id])

class center_name(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('main:center_name', args=[self.id])

class distribution(models.Model):
    center_id=models.PositiveIntegerField(default=None,null=True)
    imei=models.CharField(max_length=200,default=None, null=True)
    tablet_id=models.CharField(max_length=10,default=None,null=True)
    allotted_to=models.CharField(max_length=100, default=None, null=True)
    start_date=models.DateField(default=datetime.date.today, null=True)
    end_date=models.DateField(default=datetime.date.today, null=True)
    complete=models.BooleanField(default=False)
    condition=models.BooleanField(default=False)
    at=models.PositiveIntegerField(default=None,null=True)

    class Meta:
        ordering=('start_date',)

    def get_absolute_url(self):
        return reverse('main:distribution', args=[self.id])

class chennai(models.Model):
    center_id=models.PositiveIntegerField(default=None, null=True)
    imei=models.CharField(max_length=15, null=True, default=None)
    t_id=models.CharField(max_length=10,  null=True, default=None)
    date=models.DateField(default=datetime.date.today, null=True)
    receive_date=models.DateField(default=None,null=True)
    received=models.BooleanField(default=False)
    at=models.PositiveIntegerField(default=None,null=True)

    class Meta:
        ordering=('date',)

    def get_absolute_url(self):
        return reverse('main:detail', args=[self.id])
