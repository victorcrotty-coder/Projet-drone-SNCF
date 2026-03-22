from django.db import models


class Contact(models.Model):
    nom = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} <{self.email}>"


class Accueil(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    actif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


class Mission(models.Model):
    STATUS_CHOICES = [
        ("PLANIFIEE", "Planifiée"),
        ("EN_COURS", "En cours"),
        ("TERMINEE", "Terminée"),
        ("ANNULEE", "Annulée"),
    ]

    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PLANIFIEE")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


class Drone(models.Model):
    STATUS_CHOICES = [
        ("READY", "Prêt"),
        ("IN_MISSION", "En mission"),
        ("MAINTENANCE", "Maintenance"),
        ("HS", "Hors service"),
    ]

    nom = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True)
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default="READY")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Station(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    actif = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Donnees(models.Model):
    TYPE_CHOICES = [
        ("TEMPERATURE", "Température"),
        ("HUMIDITE", "Humidité"),
        ("PRESSION", "Pression"),
        ("VENT", "Vent"),
        ("AUTRE", "Autre"),
    ]

    type_donnee = models.CharField(max_length=20, choices=TYPE_CHOICES)
    valeur = models.FloatField()
    unite = models.CharField(max_length=50)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type_donnee}: {self.valeur} {self.unite}"


class Message(models.Model):
    TYPE_CHOICES = [
        ("INFO", "Information"),
        ("ALERTE", "Alerte"),
        ("ERREUR", "Erreur"),
    ]

    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    type_message = models.CharField(max_length=20, choices=TYPE_CHOICES, default="INFO")
    lu = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
