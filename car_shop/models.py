from django.db import models
from django.core.validators import MinValueValidator


class Marque(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='marques/', blank=True, null=True)

    def __str__(self):
        return self.nom


class Vehicule(models.Model):
    CHOIX_ENERGIE = [
        ('ESSENCE', 'Essence'),
        ('DIESEL', 'Diesel'),
        ('ELECTRIQUE', 'Électrique'),
        ('HYBRIDE', 'Hybride'),
    ]

    CHOIX_BOITE = [
        ('MANUELLE', 'Manuelle'),
        ('AUTOMATIQUE', 'Automatique'),
    ]

    titre = models.CharField(max_length=200)
    marque = models.ForeignKey(Marque, on_delete=models.CASCADE, related_name='vehicules')
    modele = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    annee = models.PositiveIntegerField()
    kilometrage = models.PositiveIntegerField()
    energie = models.CharField(max_length=20, choices=CHOIX_ENERGIE)
    boite_vitesse = models.CharField(max_length=20, choices=CHOIX_BOITE)
    description = models.TextField()
    image_principale = models.ImageField(upload_to='vehicules/principales/')
    est_disponible = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee})"


class Contact(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, related_name='contacts')
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact de {self.nom} pour {self.vehicule}"