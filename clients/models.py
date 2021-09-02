from django.db import models
from django.db.models.fields import CharField
from .model_choices import education_choices, res_choices, status_choices
from django import forms

# Create your models here.

class industryChoices(models.Model):
  ind = models.CharField(max_length=100)

  def __str__(self):
    return self.ind

class positionChoices(models.Model):
  pos = models.CharField(max_length=100)

  def __str__(self):
    return self.pos

class client(models.Model):
  name = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  phone_number = models.CharField(max_length=50)
  experience = models.IntegerField()
  industry = models.ForeignKey(industryChoices, on_delete=models.CASCADE, related_name='industries+')
  position = models.ForeignKey(positionChoices, on_delete=models.CASCADE, related_name='positions+')
  education = models.CharField(max_length=100, choices=education_choices)
  resume = models.FileField()
  residency = models.CharField(max_length=50, choices=res_choices)
  status = models.CharField(max_length=50, choices=status_choices, default='N/A')

  def __str__(self):
      return f'{self.name}'
  



