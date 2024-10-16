from django.db import models
from django import forms
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Village(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

class Chef(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    duree_fonction = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    

class Offre(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=50)
    duree = models.IntegerField()  # Par exemple, "3 mois", "1 an"
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.titre
    
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.rating}'


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    education = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='default.jpg')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"