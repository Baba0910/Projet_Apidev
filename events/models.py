from django.db import models

class Event(models.Model):
    nom = models.CharField(max_length=255)
    date = models.DateTimeField()
    max_participants = models.IntegerField()

    def __str__(self):
        return f"{self.nom} - {self.date.strftime('%d/%m/%Y')}"

class Inscription(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="inscriptions")
    prénom= models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    nombre_de_places = models.PositiveIntegerField(default=1)
    age = models.PositiveIntegerField(null=True, blank=True) 

    def __str__(self):
        return f"{self.prénom} {self.nom} - {self.event.nom}"

class Accompagnant(models.Model):
    inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE, related_name="accompagnants")
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"Accompagnant ({self.age} ans) pour {self.inscription.prénom}"

