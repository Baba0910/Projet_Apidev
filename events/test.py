from django.test import TestCase
from .models import Event, Inscription, Accompagnant
from datetime import datetime
from django.utils.timezone import make_aware

class InscriptionModelTest(TestCase):
    def setUp(self):
        # Création d'un événement pour les tests
        self.event = Event.objects.create(nom='Meetup', date=make_aware(datetime(2025, 6, 15)), max_participants=100)

    def test_create_inscription_with_accompagnant(self):
        # Test de l'inscription d'un utilisateur avec un accompagnant
        inscription = Inscription.objects.create(
            event=self.event,
            prénom="Ahmed",
            nom="Kane",
            email="ahmed@example.com",
            nombre_de_places=2,
            age=20
        )
        
        # Créer l'accompagnant associé à l'inscription
        accompagnant = Accompagnant.objects.create(
            inscription=inscription,
            age=25  # L'âge de l'accompagnant
        )

        # Vérifications
        self.assertEqual(inscription.prénom, "Ahmed")
        self.assertEqual(inscription.nom, "Kane")
        self.assertEqual(inscription.nombre_de_places, 2)
        self.assertEqual(accompagnant.age, 25)
        self.assertEqual(accompagnant.inscription, inscription)

    def test_total_places(self):
    
        # Test que le nombre total de places est bien pris en compte (participant + accompagnant)
        inscription = Inscription.objects.create(
            event=self.event,
            prénom="John",
            nom="Doe",
            email="john@example.com",
            nombre_de_places=2,
            age=30
        )

        # Créer un accompagnant
        accompagnant = Accompagnant.objects.create(
            inscription=inscription,
            age=40
        )

        # Vérification que l'accompagnant est bien associé et que le nombre total de places est correct
        self.assertEqual(inscription.nombre_de_places, 2)
        self.assertEqual(inscription.accompagnants.count(), 1)  # Un accompagnant
        self.assertEqual(accompagnant.age, 40)
