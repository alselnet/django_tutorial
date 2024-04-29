from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = "HH"
        SYNTH_POP = "SP"
        ALTERNATIVE_ROCK = "AR"
        PROG_ROCK = "PR"
        ELECTRONIC_DANCE_MUSIC = "EDM"

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5, default="HH")
    biography = models.fields.CharField(max_length=1000, default="", blank=True)
    year_formed = models.fields.IntegerField(
		validators=[MinValueValidator(1900), MaxValueValidator(2024)],
        default=2000
	)
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"

class Listing(models.Model):
    
    class Type(models.TextChoices):
        RECORDS = "REC"
        CLOTHING = "CL"
        POSTERS = "PO"
        MISCELLANEOUS = "MISC"

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000, default="", null=True, blank=True)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)],
        default=2000
	)
    type = models.fields.CharField(choices=Type.choices, max_length=5, default="MISC")
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title}"
