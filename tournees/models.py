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

class Batterie(models.Model):
    ETAT_CHOICES = [
        ("OK", "OK"),
        ("USUREE", "Usurée"),
        ("HS", "Hors service"),
    ]

    reference = models.CharField(max_length=100)
    capacite_mah = models.IntegerField()
    cycles = models.IntegerField()
    etat = models.CharField(max_length=10, choices=ETAT_CHOICES)

    def __str__(self):
        return self.reference
    
 # --------------------
# SITE
# --------------------
class Site(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.nom


# --------------------
# MISSION
# --------------------
class Mission(models.Model):
    STATUS_CHOICES = [
        ("PLANIFIEE", "Planifiée"),
        ("EN_COURS", "En cours"),
        ("TERMINEE", "Terminée"),
        ("ANNULEE", "Annulée"),
    ]

    titre = models.CharField(max_length=100)
    objectif = models.TextField()
    date_prevue = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre


# --------------------
# VOL
# --------------------
class Vol(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)

    debut = models.DateTimeField()
    fin = models.DateTimeField()
    duree_min = models.FloatField()
    distance_m = models.FloatField()
    altitude_max_m = models.FloatField()

    def __str__(self):
        return f"Vol {self.id}"


# --------------------
# MAINTENANCE
# --------------------
class Maintenance(models.Model):
    TYPE_CHOICES = [
        ("PREVENTIVE", "Préventive"),
        ("CORRECTIVE", "Corrective"),
    ]

    STATUS_CHOICES = [
        ("OUVERTE", "Ouverte"),
        ("CLOTUREE", "Clôturée"),
    ]

    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    date = models.DateTimeField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    commentaire = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Maintenance {self.id}"


# --------------------
# PIECE
# --------------------
class Piece(models.Model):
    nom = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    prix = models.FloatField()

    def __str__(self):
        return self.nom


# --------------------
# MAINTENANCE_PIECE
# --------------------
class MaintenancePiece(models.Model):
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    quantite = models.IntegerField()


# --------------------
# DRONE_BATTERIE
# --------------------
class DroneBatterie(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    batterie = models.ForeignKey(Batterie, on_delete=models.CASCADE)

    montee_le = models.DateTimeField()
    demontee_le = models.DateTimeField(null=True, blank=True)
