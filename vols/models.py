from django.db import models

class Voiture(models.Model):
    AVAILABILITY_CHOICES = [
        ('available', 'Disponible'),
        ('unavailable', 'Indisponible'),
        ('maintenance', 'Maintenance'),
    ]

    idVoiture = models.CharField(primary_key=True, max_length=50)
    vehicleType = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    pricePerDay = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
    driverIncluded = models.BooleanField()
    driverName = models.CharField(max_length=100, blank=True, null=True)
    driverPhone = models.CharField(max_length=50, blank=True, null=True)
    features = models.JSONField(default=list)  # Liste des options ou caractéristiques
    location = models.CharField(max_length=255)
    description = models.TextField()
    lastUsed = models.DateField(blank=True, null=True)
    images = models.JSONField(default=list, blank=True, null=True)  # URLs ou chemins vers les images
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'voitures'
