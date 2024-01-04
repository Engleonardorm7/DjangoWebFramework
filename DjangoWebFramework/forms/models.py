from django.db import models
from django.contrib import admin

class Logger(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    time_log=models.TimeField(help_text="Enter the exact time!")

class Person(models.Model): 
    last_name = models.TextField() 
    first_name = models.TextField() 
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

