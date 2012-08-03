from django.db import models

# Create your models here.

class Contact(models.Model):
    TITLE_CHOICES = (
        ('Sr.', 'Sr.'),
        ('Srita.', 'Srita.'),
        ('Lic.', 'Lic.'),
        ('Ing.', 'Ing.'),
    )
    name = models.CharField("Nombre", max_lenght=50)
    last_name = models.CharField("Apellido", max_lenght=30)
    email = models.EmailField("Correo Electrónico")
    title = models.CharField("Título", max_lenght=5, choices=TITLE_CHOICES)
    company = models.CharField("Empresa", max_lenght=50, blank=True)
    
    class Meta:
        abstract = True
        
class Acount(Contact):
    pass

class Customer(Contact):
    pass

class Quotation(models.Model):
    pass

class Invoice(models.Model):
    pass