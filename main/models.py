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
    
    class Meta:
        verbose_name = "Cuenta"

class Customer(Contact):
    rfc = models.CharField("RFC", max_lenght=13, blank=True)
    
    class Meta:
        verbose_name = "Cliente"

class Quotation(models.Model):
    customer = models.ForeignKey('Contact')
    
    class Meta:
        verbose_name = "Cotización"

class Invoice(models.Model):
    customer = models.ForeignKey('Customer')
    
    class Meta:
        verbose_name = "Factura"