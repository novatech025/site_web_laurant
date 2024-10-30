from django.db import models


# Create your models here.


class Sable(models.Model):
    TYPE_DE_SABLE_CHOICES = [
        ('SABLE SANAGA', 'SABLE SANAGA'),
        ('SABLE FIN', 'SABLE FIN'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_DE_SABLE_CHOICES, verbose_name="Type de sable")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    description = models.TextField()
    def __str__(self):
        return self.type

class Service(models.Model):
    sable = models.ForeignKey(Sable, on_delete=models.CASCADE, verbose_name='Sable')
    name = models.CharField(max_length=100, verbose_name="nom")
    description = models.TextField()
    image = models.ImageField(upload_to='services/', null=True, blank=True)

    def __str__(self):
        return self.name

class Realisation(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Service')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='realisations/', null=True, blank=True)

    def __str__(self):
        return self.title
