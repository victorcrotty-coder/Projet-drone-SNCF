from django.db import models

class Drone(models.Model):
    STATUS_CHOICES = [
        ("READY", "Ready"),
        ("IN_MISSION", "In mission"),
        ("MAINTENANCE", "Maintenance"),
        ("HS", "Hors service"),
    ]

    nom = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True)
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom