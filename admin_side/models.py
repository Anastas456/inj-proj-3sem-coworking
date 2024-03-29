from django.db import models

STATUS_DEALS_CHOICES = [
    ('под', 'подписан'),
    ('раб', 'в работе'),
    ('вып', 'выполнен'),
]

class Tenants(models.Model):
    tenant_name=models.CharField(max_length=255, default='ФИО или название компании')
    tenant_type = models.CharField(max_length=255)             
    phone = models.CharField(max_length=255)                  
    email = models.CharField(max_length=255)   

    def __str__(self):
        return str({self.tenant_name, self.tenant_type})           

class Individuals(models.Model):
    tenant = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, null=True)
    passport_series = models.IntegerField(max_length=4)
    passport_number = models.IntegerField(max_length=6)

    def __str__(self):
        return self.surname

class Entits(models.Model):
    tenant = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    company_name = models.TextField()
    inn = models.IntegerField(max_length=10)
    ogrn = models.IntegerField(max_length=13)
    address= models.TextField()

    def __str__(self):
        return self.company_name 

class Individual_entrepreneurs(models.Model):
    tenant = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, null=True)
    address = models.TextField()
    inn = models.PositiveIntegerField(max_length=12)
    ogrnip = models.IntegerField(max_length=15)

    def __str__(self):
        return self.surname 


class Discount_cards(models.Model):
    tenant = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    discount = models.PositiveIntegerField()

    def __str__(self):
        return str(self.discount )

class Deals(models.Model):
    tenant = models.ForeignKey('Tenants', on_delete=models.CASCADE)
    rate = models.ForeignKey('client_side.Rates', on_delete=models.CASCADE)
    premise = models.ForeignKey('client_side.Premises', on_delete=models.CASCADE)
    additional_services = models.ForeignKey('client_side.Additional_services', on_delete=models.CASCADE, blank=True, null=True)
    start_of_lease = models.DateField(auto_now_add=True)         
    end_of_lease = models.DateField(auto_now_add=True)
    date_of_signing_the_deal = models.DateField(auto_now_add=True)
    discount = models.ForeignKey('Discount_cards', on_delete=models.CASCADE, blank=True, null=True)
    total_price = models.PositiveIntegerField()
    status=models.CharField(max_length=100, choices=STATUS_DEALS_CHOICES, default='под')

    def __str__(self):
        return str(self.tenant) 