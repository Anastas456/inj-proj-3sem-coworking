from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class Premises(models.Model):
    # id = models.AutoField()
    premise_type = models.ForeignKey('Premises_types', on_delete=models.CASCADE)
    square = models.PositiveIntegerField()
    number_of_workplaces = models.PositiveIntegerField()
    address = models.TextField()

    def __str__(self):
        return str(self.premise_type)

class Premises_types(models.Model):
    # id = models.AutoField()
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type

class Rates(models.Model):
    # id = models.AutoField()
    premise_type = models.ForeignKey('Premises_types', on_delete=models.CASCADE)
    rental_time = models.CharField(max_length=255)
    fixed_or_non_fixed = models.BooleanField(default=False)
    price = models.PositiveIntegerField()

    def __str__(self):
        return str(self.price)

class Additional_services(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Rent_form(models.Model):
    client_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)  
    description = models.TextField()

    def __str__(self):
        return self.client_name