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

class Message_User(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(default = 'kfb@gmail.com')
    message = models.TextField(default = 'message')
    date_send = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Testimonial(models.Model):
    name = models.CharField(max_length=100,verbose_name="Nom")
    photo = models.ImageField(upload_to='testimonials/')
    role = models.CharField(max_length=100 , verbose_name="Métier")
    comment = models.TextField(verbose_name="Commentaire")
    stars = models.PositiveIntegerField(default=5,verbose_name="étoiles")

    def __str__(self):
        return f"{self.name} - {self.role}"

    def get_star_rating(self):
        return "★" * self.stars + "☆" * (5 - self.stars)

    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"
        ordering = ['-id']