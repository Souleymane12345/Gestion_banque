from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DonneCommune (models.Model):
    email = models.EmailField(max_length=225)
    numero = models.ImageField()
    password = models.CharField(max_length= 50)
    address = models.CharField(max_length=100)
   


    class Meta: 
        abstract:True

class Banque(DonneCommune):
    
    statut_moral = models.CharField(max_length=50)
    identifiant = models.CharField(max_length=25)



class Client(DonneCommune):
    
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=50)
    compte = models.CharField(max_length=25)
    montant = models.IntegerField()
    identifiant = models.CharField(max_length=25)


class Agent(DonneCommune):

    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=50)
    identifiant = models.CharField(max_length=25)

class Compte(models.Model): 
    numero_compte = models.CharField(max_length=25)
    
    



