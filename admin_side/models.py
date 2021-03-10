from django.db import models
from client_side.models import Rates, Premises, Additional_services

# Create your models here.


class Tenants(models.Model):
    # id = models.AutoField()
    tenant_type = models.CharField(max_length=255)             
    phone = models.CharField(max_length=15)                  
    email = models.CharField(max_length=255)   

    def __str__(self):
        return self.tenant_type               

class Individuals(models.Model):
    # id = models.AutoField()
    tenant = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, null=True)
    passport_series = models.IntegerField(max_length=4)
    passport_number = models.IntegerField(max_length=6)

    def __str__(self):
        return self.surname

class Entits(models.Model):
    # id = models.AutoField()
    tenant = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    company_name = models.TextField()
    inn = models.IntegerField(max_length=10)
    ogrn = models.IntegerField(max_length=13)
    address= models.TextField()

    def __str__(self):
        return self.company_name 

class Individual_entrepreneurs(models.Model):
    # id = models.AutoField()
    tenant = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, null=True)
    address = models.TextField()
    inn = models.PositiveIntegerField(max_length=12)
    ogrnip = models.IntegerField(max_length=15)

    def __str__(self):
        return self.surname 

# class Premises(models.Model):
#     # id = models.AutoField()
#     premise_type = models.ForeignKey('Premises_types', on_delete=models.CASCADE)
#     square = models.PositiveIntegerField()
#     number_of_workplaces = models.PositiveIntegerField()
#     address = models.TextField()

#     def __str__(self):
#         return self.premise_type 

# class Premises_types(models.Model):
#     # id = models.AutoField()
#     type = models.CharField(max_length=255)

#     def __str__(self):
#         return self.type

# class Rates(models.Model):
#     # id = models.AutoField()
#     premise_type = models.ForeignKey('Premises_types', on_delete=models.CASCADE)
#     rental_time = models.CharField(max_length=255)
#     fixed_or_non_fixed = models.BooleanField(default=False)
#     price = models.PositiveIntegerField()

#     def __str__(self):
#         return self.price

# class Additional_services(models.Model):
#     # id = models.AutoField()
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.PositiveIntegerField()

#     def __str__(self):
#         return self.name

class Discount_cards(models.Model):
    # id = models.AutoField()
    tenant = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    discount = models.PositiveIntegerField()

    def __str__(self):
        return self.discount 

class Deals(models.Model):
    # id = models.AutoField()
    tenant = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    rate = models.ForeignKey('client_side.Rates', on_delete=models.CASCADE)
    premise = models.ForeignKey('client_side.Premises', on_delete=models.CASCADE)
    additional_services = models.ForeignKey('client_side.Additional_services', on_delete=models.CASCADE, null=True)
    start_of_lease = models.DateField(auto_now_add=True)         #доп опции в скобках ???
    end_of_lease = models.DateField(auto_now_add=True)
    date_of_signing_the_deal = models.DateField(auto_now_add=True)
    discount = models.ForeignKey('Discount_cards', on_delete=models.CASCADE, null=True)
    total_price = models.PositiveIntegerField()

    def __str__(self):
        return self.total_price 