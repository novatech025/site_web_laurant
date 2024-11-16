from django.db import models


# Create your models here.


class Realisation(models.Model):
    types=[
    ('SABLE SANAGA','SABLE SANAGA'),
    ('SABLE FIN','SABLE FIN')
    ]
    sable=models.CharField(choices=types,max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='realisations/', null=True, blank=True)

    def __str__(self):
        return self.sable

class Message_User(models.Model):
    name = models.CharField(max_length = 30, default = 'inconnu')
    email = models.EmailField(default = 'kfb@gmail.com')
    message = models.TextField(default = 'message')
    date_send = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Testimonial(models.Model):
    RATE_LEVEL = (
        (0, "Très mécontent", ),
        (1, "Mécontent", ),
        (2, "Indifférent",),
        (3, "Satisfait",),
        (4, "Assez Satisfait",),
        (5, "Très Satisfait",),
        )
    name = models.CharField(max_length=100,verbose_name="Nom")
    photo = models.ImageField(upload_to='testimonials/')
    role = models.CharField(max_length=100 , verbose_name="Métier")
    comment = models.TextField(max_length=210,verbose_name="Commentaire")
    stars = models.PositiveIntegerField(choices=RATE_LEVEL, default=5,verbose_name="étoiles")
    published = models.BooleanField(default=True, verbose_name="publié")

    def __str__(self):
        return f"{self.name} - {self.role}"

    def get_star_rating(self):
        return "★" * self.stars + "☆" * (5 - self.stars)

    def get_colored_rate_list(self):
        return [i for i in range(self.stars)]
    

    def get_uncolored_rate_list(self):
        return [i for i in range(5 - self.stars)]
    
    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"
        ordering = ['-id']
